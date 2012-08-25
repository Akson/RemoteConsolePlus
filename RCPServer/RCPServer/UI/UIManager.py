'''Created by Dmytro Konobrytskyi, 2012(C)'''
from ControlPanel.ControlPanelWindow import ControlPanelWindow
import wx

class UIManager(object):
    '''UIManager controls windows visibility and UI related stuff'''

    def __init__(self):
        #Create control panel
        self._controlPanel = ControlPanelWindow()
        self._controlPanel.Bind(wx.EVT_CLOSE, self.OnWindowClose)        
        
        #List of all output windows
        self._outputWindows = dict()

    def OnWindowClose(self, event):
        exit()
    
    def ShowControlPanel(self):
        self._controlPanel.Show()

    def ShowOutputWindow(self, windowName):
        self._outputWindows[windowName].Show()
        
    def RegisterNewOutputWindow(self, outputWindow, windowName):
        self._outputWindows[windowName] = outputWindow
        outputWindow.Bind(wx.EVT_CLOSE, self.OnWindowClose)
        self._outputWindows[windowName].Show()        
