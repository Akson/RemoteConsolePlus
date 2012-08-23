'''Created by Dmytro Konobrytskyi, 2012(C)'''
from RCPServer.UI.OutputWindow.HTMLConsole import HTMLConsole

class OutputRouter(object):
    '''Class description...'''

    def __init__(self, uiManager):
        self._uiManager = uiManager
        
        #Create and register default console
        self._uiManager.RegisterNewOutputWindow(HTMLConsole("Default console"), "")

    def PassMessage(self, message):
        self._uiManager.PassMessage(message, "")