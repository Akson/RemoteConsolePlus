'''Created by Dmytro Konobrytskyi, 2012(C)'''
import json
import copy
from RCPServer.ConfigManager.ConfigManager import MessageConfig

class ProtocolParser(object):
    '''
    Implementation of a standard JSON based protocol
    with additional data after JSON message.
    '''

    def __init__(self, filterRouter):
        self._router = filterRouter
        self._decoder = json.JSONDecoder()
        
    def ParseProtocolMessage(self, message):
        #Parse JSON message first and add additional tail data to a result object
        messageObject, tailIndex = self._decoder.raw_decode(message)
        if tailIndex < len(message):
            messageObject["BinaryData"] = message[tailIndex:]
        
        #Create output message with all fields set to default values 
        outputMessage = copy.deepcopy(MessageConfig.DefaultMessageFields)
        outputMessage.update(messageObject)
        
        #Pass parsed data object to the router
        self._router.PassMessage(outputMessage)