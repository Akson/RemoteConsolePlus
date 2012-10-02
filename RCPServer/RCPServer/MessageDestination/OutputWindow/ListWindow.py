'''Created by Dmytro Konobrytskyi, 2012(C)'''
import wx
from RCPServer.MessageDestination.DestinationBase import DestinationBase

class ListWindow(DestinationBase, wx.Frame):
    '''
    This destination class shows a list of streams and their values
    '''
    def __init__(self, windowName):
        if windowName == "": 
            windowName = "Default console" #No name destination is default console
        wx.Frame.__init__(self, None, title=windowName)
        
        self._streamValues = {}
        self._streamsListIndexes = {}
        
        self._listCtr = wx.ListCtrl(self, style=wx.LC_REPORT|wx.BORDER_SUNKEN)
        self._listCtr.InsertColumn(0, 'StreamName', width=100)
        self._listCtr.InsertColumn(1, 'Value', width=200)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self._listCtr, 1, wx.EXPAND)
        self.SetSizer(sizer)
        
    def ProcessMessage(self, newMessage):
        streamName = newMessage["StreamName"]
        value = str(newMessage["Value"])

        #Add a new item to the list and save it's index if we don't have it yet        
        if streamName not in self._streamsListIndexes:
            newIndex = self._listCtr.GetItemCount()
            self._streamsListIndexes[streamName] = newIndex
            self._listCtr.Append([streamName, value])
            self._listCtr.SetItemBackgroundColour(newIndex, ["white", wx.Colour(240, 240, 240)][newIndex%2])
        
        #Update stream value
        index = self._streamsListIndexes[streamName]
        self._listCtr.SetStringItem(index, 1, value)
