'''Created by Dmytro Konobrytskyi, 2012(C)'''
import json

class ProtocolParser(object):
    '''
    Implementation of a standard JSON based protocol
    with additional data after JSON message.
    '''

    def __init__(self, filterRouter):
        self._filterRouter = filterRouter
        self._decoder = json.JSONDecoder()

    def ParseProtocolMessage(self, message):
        #Parse JSON message first and add additional tail data to a result object
        messageObject, tailIndex = self._decoder.raw_decode(message)
        if tailIndex < len(message):
            messageObject["AdditionalData"] = message[tailIndex:]
        
        #Pass parsed data object to the router
        self._filterRouter.PassMessage(messageObject)