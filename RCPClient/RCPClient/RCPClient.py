'''Created by Dmytro Konobrytskyi, 2012(C)'''
import zmq
import json
import time

print "RCPClient module"

class RCPConnection(object):
    _context = None
    _socket = None
    
    @staticmethod
    def SendMessage(message):
        #Check connection 
        if RCPConnection._socket == None:
            raise Exception("Attempt to send message without connection.")
        RCPConnection._socket.send(message)
        
def RCConnect(address):
    RCPConnection._context = zmq.Context()
    RCPConnection._socket = RCPConnection._context.socket(zmq.PUB)
    RCPConnection._socket.connect(address)

def RCPrint(value, streamName=None, filters=None, destinations=None):
    #Fill message fields
    messageObj = dict()
    messageObj["Value"] = value 
    messageObj["TimeStamp"] = time.time()
    if streamName: messageObj["StreamName"] = streamName 
    if filters: messageObj["Filters"] = filters 
    if destinations: messageObj["Destinations"] = destinations 

    #Convert a message to JSON format and send to a server
    RCPConnection.SendMessage(json.dumps(messageObj))