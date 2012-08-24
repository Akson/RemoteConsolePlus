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
        #Receive all incoming messages and pass them to the protocol parser
        try:
            while True:
                message = self._socket.recv(zmq.NOBLOCK)
                self._protocolParser.ParseProtocolMessage(message)
        except zmq.ZMQError:
            pass
