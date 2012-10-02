'''Created by Dmytro Konobrytskyi, 2012(C)'''
import wx.html
from RCPServer.ConfigManager.ConfigManager import HTMLConsoleConfig
from RCPServer.MessageDestination.DestinationBase import DestinationBase

class HTMLConsole(DestinationBase):
    '''
    This destination class is the default console window
    which does show messages as HTML
    '''

    def __init__(self, windowName):
        if windowName == "": 
            windowName = "Default console" #No name destination is default console
        DestinationBase.__init__(self, windowName)
        self._messagesList = []
        
        self._htmlWindow = wx.html.HtmlWindow(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self._htmlWindow, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def ProcessMessage(self, newMessage):
        #print newMessage
        
        #Save new message to buffer
        self._messagesList.append(newMessage)
        
        #Limit buffer size
        self._messagesList = self._messagesList[-HTMLConsoleConfig.ConsoleMessageBufferSize:]
        
        #Construct 
        consoleText = '<font>'
        
        for message in self._messagesList:
            if message["StreamName"] != "": consoleText += "[%(StreamName)s]: " % message
            consoleText += "%(Value)s<br>" % message

        consoleText += "</font>"

        #Update console content and scroll to the bottom
        self._htmlWindow.Freeze()    
        self._htmlWindow.SetPage(consoleText)
        self._htmlWindow.Scroll(0, self._htmlWindow.GetScrollRange(wx.VERTICAL)) 
        self._htmlWindow.Thaw()
