'''Created by Dmytro Konobrytskyi, 2012(C)'''
import wx
from Network.Server import Server
from UI.UIManager import UIManager
from MessageProcessor.InputRouter import InputRouter
from MessageProcessor.OutputRouter import OutputRouter

class RCPServer(object):
    '''Class description...'''

    def __init__(self):
        self._app = wx.App(redirect=False)  #default error output to console
        
        self._uiManager = UIManager()
        self._outputRouter = OutputRouter(self._uiManager)
        self._inputRouter = InputRouter(self._outputRouter)
        self._server = Server(self._inputRouter)
        
        self._uiManager.ShowOutputWindow("")
        #self._uiManager.ShowControlPanel()
        
        #Run main message receiving timer
        timerOwner = wx.EvtHandler()
        self._mainTimer = wx.Timer(timerOwner, wx.ID_ANY)
        self._mainTimer.Start(100)
        timerOwner.Bind(wx.EVT_TIMER, self.ProcessMessagess, self._mainTimer)
        
        self._app.MainLoop()

    def ProcessMessagess(self, event):
        self._server.ReceiveMessages()
        