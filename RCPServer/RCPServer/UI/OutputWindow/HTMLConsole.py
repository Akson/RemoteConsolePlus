'''Created by Dmytro Konobrytskyi, 2012(C)'''
import wx
import wx.html
from RCPServer.ConfigManager.ConfigManager import HTMLConsoleConfig

class HTMLConsole(wx.Frame):
    '''Class description...'''

    def __init__(self, windowName):
        wx.Frame.__init__(self, None, title=windowName)
        self._messagesList = []
        
        self._htmlWindow = wx.html.HtmlWindow(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self._htmlWindow, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def ProcessMessage(self, newMessage):
        print newMessage
        
        #Save new message to buffer
        self._messagesList.append(newMessage)
        
        #Limit buffer size
        self._messagesList = self._messagesList[-HTMLConsoleConfig.ConsoleMessageBufferSize:]
        
        #Construct 
        consoleText = ""
        for message in self._messagesList:
            consoleText += str(message["Value"])
            consoleText += "<br>"

        #Update console content and scroll to the bottom
        self._htmlWindow.Freeze()    
        self._htmlWindow.SetPage(consoleText)
        self._htmlWindow.Scroll(0, self._htmlWindow.GetScrollRange(wx.VERTICAL)) 
        self._htmlWindow.Thaw()
