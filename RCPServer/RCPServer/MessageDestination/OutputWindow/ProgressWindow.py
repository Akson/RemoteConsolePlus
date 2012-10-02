'''Created by Dmytro Konobrytskyi, 2012(C)'''
import wx
from RCPServer.MessageDestination.DestinationBase import DestinationBase

class ProgressWindow(DestinationBase):
    '''
    classdocs
    '''

    def __init__(self, windowName):
        if windowName == "":
            windowName = "Default console" #No name destination is default console
        DestinationBase.__init__(self, windowName)

        self._gauge = wx.Gauge(self, -1, 100, size=(250, 25))

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self._gauge, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def ProcessMessage(self, newMessage):
        value = int(newMessage["Value"])
        self._gauge.SetValue(value)