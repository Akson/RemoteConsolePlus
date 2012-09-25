'''Created by Dmytro Konobrytskyi, 2012(C)'''

class FilterBase(object):
    '''Class description...'''

    def __init__(self):
        self._defaultParameters = self.ConstructDefaultParameters()
        pass

    def ApplyFilterToMessage(self, message, filterParameters):
        #Combine default parameters with passed values and apply filter
        combinedFilterParameters = dict(self._defaultParameters)
        combinedFilterParameters.update(filterParameters)
        self.ApplyFilter(message, combinedFilterParameters)
        
    def ConstructDefaultParameters(self):
        return dict()

    def ApplyFilter(self, message, filterParameters):
        pass