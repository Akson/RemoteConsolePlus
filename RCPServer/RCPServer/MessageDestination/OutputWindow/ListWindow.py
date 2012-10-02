'''Created by Dmytro Konobrytskyi, 2012(C)'''
import wx
from RCPServer.MessageDestination.DestinationBase import DestinationBase

class ListWindow(DestinationBase):
    '''
    This destination class shows a list of streams and their values
    '''
    def __init__(self, windowName):
        if windowName == "": 
            windowName = "Default console" #No name destination is default console
        DestinationBase.__init__(self, windowName)
        
        self._streamValues = {}
        
        self._listCtr = wx.ListCtrl(self, style=wx.LC_REPORT|wx.BORDER_SUNKEN)
        self._listCtr.InsertColumn(0, 'StreamName', width=100)
        self._listCtr.InsertColumn(1, 'Value', width=200)
        
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
