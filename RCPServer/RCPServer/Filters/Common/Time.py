'''Created by Dmytro Konobrytskyi, 2012(C)'''
from RCPServer.Filters.Filter import Filter

class Time(Filter):
    '''
    This filter formats time value. It gets a number of milliseconds
    and outputs time in SSs MSms format by default.
    '''

    def __init__(self):
        #Call default parent constructor
        Filter.__init__(self)

    def ConstructDefaultParameters(self):
        return {"unit":"ms"}

    def ApplyFilter(self, message, filterParameters):
        #Select appropriate input units
        if filterParameters["unit"] == "ms":
            timeValueMS = float(message["Value"])
        elif filterParameters["unit"] == "s":
            timeValueMS = float(message["Value"])*1000
        elif filterParameters["unit"] == "m":
            timeValueMS = float(message["Value"])*1000*60
        
        outputStr = ""
        if timeValueMS < 1000:
            ms = int(timeValueMS)
            outputStr = "{}ms".format(ms)
        else:
            s = int(timeValueMS)/1000
            ms = int(timeValueMS)%1000
            outputStr = "{}s {}ms".format(s, ms)
        
        message["Value"] = outputStr 
