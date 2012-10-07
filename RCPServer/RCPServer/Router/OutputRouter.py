'''Created by Dmytro Konobrytskyi, 2012(C)'''
from RCPServer.MessageDestination.OutputWindow.HTMLConsole import HTMLConsole
from RCPServer.Filters.FiltersManager import FiltersManager
from RCPServer.MessageDestination.OutputWindow.ProgressWindow import ProgressWindow
import wx
from RCPServer.MessageDestination.OutputWindow.ListWindow import ListWindow
from RCPServer.MessageDestination.OutputWindow.GraphsWindow import GraphsWindow

class OutputRouter(object):
    '''Router applies all filters to a message and then route it to appropriate destinations'''

    def __init__(self, uiManager):
        self._uiManager = uiManager
        
        #List of possible message destinations
        self._destinations = dict()
        
        #Create and register default console
        defConsole = self.CreateAndRegisterNewDestination()
        
        #Add event listener in order to close the entire application when the default console is closed
        defConsole.Bind(wx.EVT_CLOSE, lambda event: exit())

    def CreateAndRegisterNewDestination(self, destinationName=""):
        #Extract destination type
        destinationType = None  #HTML console by default
        typeNameStart = destinationName.find("(")
        if typeNameStart != -1:
            destinationType = destinationName[typeNameStart+1:-1].strip(" ")
        
        #Default destination type is HTMLConsole
        newDestination = HTMLConsole(destinationName)

        if destinationType == "ProgressWindow": #Default destination type is HTMLConsole
            newDestination = ProgressWindow(destinationName)

        if destinationType == "ListWindow": #Default destination type is HTMLConsole
            newDestination = ListWindow(destinationName)

        if destinationType == "GraphsWindow": #Default destination type is HTMLConsole
            newDestination = GraphsWindow(destinationName)

        self._destinations[destinationName] = newDestination
        self._uiManager.RegisterNewOutputWindow(newDestination, destinationName)

        #Hide a destination when user closes it        
        newDestination.Bind(wx.EVT_CLOSE, lambda event: event.GetEventObject().Hide())
        
        return newDestination
    
    def DestroyAndUnregisterDestination(self, destinationName):
        if destinationName in self._destinations:
            del self._destinations[destinationName]
            self._uiManager.UnRegisterOutputWindow(destinationName)

    def PassMessage(self, message):
        #Create a list of destinations by splitting Destinations field and deleting spaces around names
        destinationsList = [name.strip(" ") for name in message["Destinations"].split(",")]
        
        #Pass message to all destinations, if a destination does not exist, create it
        for destination in destinationsList:
            if destination not in self._destinations:
                self.CreateAndRegisterNewDestination(destination)
            self._destinations[destination].ProcessMessage(message)
            #Always show window when new messages come
            self._destinations[destination].Show()
