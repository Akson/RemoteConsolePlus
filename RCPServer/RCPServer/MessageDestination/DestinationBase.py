'''Created by Dmytro Konobrytskyi, 2012(C)'''

class DestinationBase(object):
    '''
    Base class for all destinations
    '''

    def __init__(self):
        yield

    def ProcessMessage(self, newMessage):
        yield