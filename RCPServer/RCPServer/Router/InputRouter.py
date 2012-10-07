'''Created by Dmytro Konobrytskyi, 2012(C)'''
from RCPServer.Filters.Common.Time import Time
from RCPServer.Filters.Common.Font import Font
from RCPServer.Filters.Common.Bars import Bars

class InputRouter(object):
    '''Router applies all filters to a message and then route it to appropriate destinations'''

    def __init__(self, inputPipe):
        #Collector part sends processed messages to destinations via this pipe.
        self._inputPipe = inputPipe

    def PassMessage(self, message):
        #Apply all filters mentioned in the message to the message before passing it to destination
        self.ApplyFilters(message)
        try:
            self._inputPipe.send(message)
        except IOError:
            #Emitter part has exited so it's time to exit 
            exit()

    def ApplyFilters(self, message):
        filtersStr = message["Filters"]
        if filtersStr != "":
            #Construct filters list
            filtersList = [name.strip(" ") for name in filtersStr.split("|")]
            
            #Apply all filters 
            for filterDescription in filtersList:
                #Separate filter name from parameters
                filterName, filterParameters = self.ParseFilterDescription(filterDescription)
                
                #Find filter
                filterObject = self.FindFilterByName(filterName)
                if filterObject != None:
                    #Apply filter now
                    filterObject.ApplyFilterToMessage(message, filterParameters)
                elif filterName != "":
                    raise Exception("Cannot find appropriate filter: ", filterName)
        
    def ParseFilterDescription(self, filterDescription):
        try:
            parametersStartIndex = filterDescription.find("(")
            
            #Return filter name if there are no filter parameters
            if parametersStartIndex == -1:
                return filterDescription, dict() 
    
            #Parse parameters and construct a dictionary with all parameters        
            filterName = filterDescription[:parametersStartIndex]
            filterParametersStr = filterDescription[parametersStartIndex+1:-1]
            parametersPairsList = [name.strip(" ") for name in filterParametersStr.split(",")]

            parametersDict = dict()
            for parameterPairStr in parametersPairsList:
                parameterPair = parameterPairStr.split("=")
                parametersDict[parameterPair[0]] = parameterPair[1]
            
            return filterName, parametersDict
        except:
            raise Exception("Cannot parse filter name and/or parameters: ", filterDescription)
    
    def FindFilterByName(self, filterName):
        if filterName == "Time": return Time()
        if filterName == "Font": return Font()
        if filterName == "Bars": return Bars()
        return None