'''Created by Dmytro Konobrytskyi, 2012(C)'''

class FilterRouter(object):
    '''Class description...'''

    def __init__(self, outputRouter):
        self._outputRouter = outputRouter

    def PassMessage(self, message):
        self._outputRouter.PassMessage(message)