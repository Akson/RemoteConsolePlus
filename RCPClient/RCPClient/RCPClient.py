'''Created by Dmytro Konobrytskyi, 2012(C)'''
import zmq
import json
import time

class RCPClient(object):
    _context = None
    _socket = None

    @staticmethod
    def Connect(address):
        RCPClient._context = zmq.Context()
        RCPClient._socket = RCPClient._context.socket(zmq.PUB)
        RCPClient._socket.connect(address)
    
    @staticmethod
    def _SendMessage(message):
        if RCPClient._socket == None:
            raise Exception("Attempt to send message without connection.")
        RCPClient._socket.send(message)
        
    @staticmethod
    def Print(value):
        message = json.dumps({"Stream":"TestStream", "Value":value, "TimeStamp":str(time.time()) })
        RCPClient._SendMessage(message+"some extrea tail data")        
        RCPClient._SendMessage(message)