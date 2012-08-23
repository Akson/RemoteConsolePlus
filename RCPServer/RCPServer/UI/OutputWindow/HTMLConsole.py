'''Created by Dmytro Konobrytskyi, 2012(C)'''
import wx

class HTMLConsole(wx.Frame):
    '''Class description...'''

    def __init__(self, windowName):
        wx.Frame.__init__(self, None, title=windowName)

    def ProcessMessage(self, message):
        print message