'''Created by Dmytro Konobrytskyi, 2012(C)'''
import wx

class DestinationBase(wx.Frame):
    '''
    Base class for all destination windows
    '''

    def __init__(self, windowName):
        wx.Frame.__init__(self, None, title=windowName)

    def ProcessMessage(self, newMessage):
        yield

    def GetWindowProperties(self):
        return {}

    def SetWindowProperties(self, windowProperties):
        yield