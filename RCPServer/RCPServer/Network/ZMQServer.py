'''Created by Dmytro Konobrytskyi, 2012(C)'''

import zmq
from RCPServer.ConfigManager.ConfigManager import NetworkConfig

class ZMQServer(object):
    '''
    Server is used for receiving messages over network from clients.
    '''

    def __init__(self):
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.SUB)
        self._socket.bind(NetworkConfig.NetworkAddress)
        self._socket.setsockopt(zmq.SUBSCRIBE, "")
        
    def ReceiveMessages(self):
        return self._socket.recv()
