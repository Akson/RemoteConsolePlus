'''Created by Dmytro Konobrytskyi, 2012(C)'''

class Server(object):
    '''Server is used for receiving messages over network from clients'''

    def __init__(self, inputRouter):
        self._inputRouter = inputRouter
        
    def ReceiveMessages(self):
        message = "test"
        self._inputRouter.PassMessage(message)