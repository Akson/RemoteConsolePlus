'''Created by Dmytro Konobrytskyi, 2012(C)'''
from ControlPanel.ControlPanelWindow import ControlPanelWindow
import wx
from RCPServer.ConfigManager.ConfigManager import UIConfig
import json

class UIManager(object):
    '''UIManager controls windows visibility and UI related stuff'''

    def __init__(self):
        #Create control panel
        self._controlPanel = ControlPanelWindow()
        
        #List of all output windows
        self._outputWindows = dict()
        
        #Here we are going to store positions and sizes of all windows
        #in order to have them the same as last launch when applications starts
        self._windowsPositions = dict()
        
        #Load stored windows positions
        try:
            winConfigFile = open(UIConfig.WindowsPositionsFileName, "r")
            storedWindowsPositions = json.load(winConfigFile)
            self._windowsPositions.update(storedWindowsPositions)
            winConfigFile.close()
        except:
            pass    #We don't really care if there is no config files
        
    def SaveWindowsPositions(self):
        for windowName in self._outputWindows:
            curWin = self._outputWindows[windowName]
            pos = curWin.GetPosition()
            size = curWin.GetSize()
            windowProperties = curWin.GetWindowProperties()
            self._windowsPositions[windowName] = {'pos':[pos[0], pos[1]], 'size':[size[0], size[1]], 'windowProperties':windowProperties}
            
        winConfigFile = open(UIConfig.WindowsPositionsFileName, "w")
        json.dump(self._windowsPositions, winConfigFile, indent = 4)
        winConfigFile.close()
         
    def ShowControlPanel(self):
        self._controlPanel.Show()

    def ShowOutputWindow(self, windowName):
        self._outputWindows[windowName].Show()
    
    def SaveWindowPositions(self, event):
        self.SaveWindowsPositions()
        event.Skip()

    def RegisterNewOutputWindow(self, outputWindow, windowName):
        self._outputWindows[windowName] = outputWindow
        outputWindow.Bind(wx.EVT_MOVE, self.SaveWindowPositions)
        outputWindow.Bind(wx.EVT_SIZING, self.SaveWindowPositions)
        
        #Try to load stored window position
        if windowName in self._windowsPositions:
            pos = self._windowsPositions[windowName]['pos']
            size = self._windowsPositions[windowName]['size']
            self._outputWindows[windowName].SetPosition((pos[0], pos[1]))
            self._outputWindows[windowName].SetSize((size[0], size[1]))
            windowProperties = self._windowsPositions[windowName]['windowProperties']
            self._outputWindows[windowName].SetWindowProperties(windowProperties)

        self._outputWindows[windowName].Show()        

    def UnRegisterOutputWindow(self, windowName):
        self._outputWindows[windowName].Hide()
        del self._outputWindows[windowName]

