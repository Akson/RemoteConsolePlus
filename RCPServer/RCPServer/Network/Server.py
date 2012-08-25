'''Created by Dmytro Konobrytskyi, 2012(C)'''

import zmq
from RCPServer.ConfigManager.ConfigManager import NetworkConfig

class Server(object):
    '''
    Server is used for receiving messages over network from clients.
    '''

    def __init__(self, protocolParser):
        self._protocolParser = protocolParser

        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.SUB)
        self._socket.bind(NetworkConfig.NetworkAddress)
        self._socket.setsockopt(zmq.SUBSCRIBE, "")
        
    def ReceiveMessages(self):
        messagesList = []
        try:
        #Receive all incoming messages and pass them to the protocol parser
            while True:
                message = self._socket.recv(zmq.NOBLOCK)
                messagesList.append(message)
        except zmq.ZMQError: #We get an exception when the incoming buffer is empty
            #Skip all messages except last. It's useful if we have too many message waiting in buffer
            messagesList = messagesList[-NetworkConfig.ProcessLastMessages:]
            #Process all message
            for message in messagesList:
                self._protocolParser.ParseProtocolMessage(message)
