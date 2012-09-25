'''Created by Dmytro Konobrytskyi, 2012(C)'''
from RCPServer.Filters.Common.Time import Time
from RCPServer.Filters.Common.Font import Font

class FiltersManager(object):
    '''Class description...'''

    def __init__(self):
        pass

    def FindFilterByName(self, filterName):
        if filterName == "Time": return Time()
        if filterName == "Font": return Font()
        return None