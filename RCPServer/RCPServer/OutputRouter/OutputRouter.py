'''Created by Dmytro Konobrytskyi, 2012(C)'''
from RCPServer.MessageDestination.OutputWindow.HTMLConsole import HTMLConsole

class OutputRouter(object):
    '''Class description...'''

    def __init__(self, uiManager):
        self._uiManager = uiManager
        
        #List of possible message destinations
        self._destinations = dict()
        
        #Create and register default console
        self.CreateNewDestination()

    def CreateNewDestination(self, destinationName="", destinationType=None):
        if destinationType == None: #Default destination type is HTMLConsole
            newDestination = HTMLConsole(destinationName)
            self._destinations[destinationName] = newDestination
            self._uiManager.RegisterNewOutputWindow(newDestination, destinationName)

    def PassMessage(self, message):
        #Create a list of destinations by splitting Destinations field and deleting spaces around names
        destinationsList = [name.strip(" ") for name in message["Destinations"].split(",")]
        
        #Pass message to all destinations
        for destination in destinationsList:
            print destination
            if destination not in self._destinations:
                self.CreateNewDestination(destination)
            self._destinations[destination].ProcessMessage(message)
