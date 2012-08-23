'''Created by Dmytro Konobrytskyi, 2012(C)'''
from ControlPanel.ControlPanelWindow import ControlPanelWindow
from RCPServer.UI.OutputWindow.HTMLConsole import HTMLConsole
import wx

class UIManager(object):
    '''UIManager controls windows visibility and UI related stuff'''

    def __init__(self):
        self._controlPanel = ControlPanelWindow()
        self._controlPanel.Bind(wx.EVT_CLOSE, self.OnWindowClose)        
        
        self._outputWindows = dict()
        
        self._outputWindows[""] = HTMLConsole("Default console")
        self._outputWindows[""].Bind(wx.EVT_CLOSE, self.OnWindowClose)        
    
    def GetControlPanel(self):
        return self._controlPanel 
    
    def ShowControlPanel(self):
        self._controlPanel.Show()

    def ShowOutputWindow(self, windowName):
        self._outputWindows[windowName].Show()
        
    def OnWindowClose(self, event):
        exit()

    def PassMessage(self, message, window):
        self._outputWindows[window].ProcessMessage(message)