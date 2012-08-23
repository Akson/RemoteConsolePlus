'''Created by Dmytro Konobrytskyi, 2012(C)'''

class OutputRouter(object):
    '''Class description...'''

    def __init__(self, uiManager):
        self._uiManager = uiManager

    def PassMessage(self, message):
        self._uiManager.PassMessage(message, "")