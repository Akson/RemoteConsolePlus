'''Created by Dmytro Konobrytskyi, 2012(C)'''
import wx

class ProgressWindow(wx.Frame):
    '''
    classdocs
    '''

    def __init__(self, windowName):
        if windowName == "":
            windowName = "Default console" #No name destination is default console
        wx.Frame.__init__(self, None, title=windowName)

        self._gauge = wx.Gauge(self, -1, 100, size=(250, 25))

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self._gauge, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def ProcessMessage(self, newMessage):
        value = int(newMessage["Value"])
        self._gauge.SetValue(value)

