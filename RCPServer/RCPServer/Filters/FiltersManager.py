'''Created by Dmytro Konobrytskyi, 2012(C)'''
from RCPServer.Filters.Common.Time import Time
from RCPServer.Filters.Common.Font import Font
from RCPServer.Filters.Common.Bars import Bars

class FiltersManager(object):
    '''Filter manager returns an appropriate filter object by name'''

    def __init__(self):
        pass

    def FindFilterByName(self, filterName):
        if filterName == "Time": return Time()
        if filterName == "Font": return Font()
        if filterName == "Bars": return Bars()
        return None