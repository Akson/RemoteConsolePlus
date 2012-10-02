'''Created by Dmytro Konobrytskyi, 2012(C)'''
import wx

class ListWindow(wx.Frame):
    '''
    This destination class shows a list of streams and their values
    '''
    def __init__(self, windowName):
        if windowName == "": 
            windowName = "Default console" #No name destination is default console
        wx.Frame.__init__(self, None, title=windowName)
        
        self._streamValues = {}
        
        self._listCtr = wx.ListCtrl(self, style=wx.LC_REPORT|wx.BORDER_SUNKEN)
        self._listCtr.InsertColumn(0, 'StreamName')
        self._listCtr.InsertColumn(1, 'Value')
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self._listCtr, 1, wx.EXPAND)
        self.SetSizer(sizer)
        
    def ProcessMessage(self, newMessage):
        #Update list values
        self._streamValues[newMessage["StreamName"]] = newMessage["Value"]
        
        #Generate list
        self._listCtr.DeleteAllItems()
        for streamName, value in self._streamValues.iteritems():
            self._listCtr.Append([streamName, value])
