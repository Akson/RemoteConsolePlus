'''Created by Dmytro Konobrytskyi, 2012(C)'''
import json
from RCPServer.FilterRouter.FiltersManager import FiltersManager

class FilterRouter(object):
    '''Class description...'''

    def __init__(self, outputRouter):
        self._outputRouter = outputRouter
        self._filtersManager = FiltersManager()

    def PassMessage(self, message):
        filtersStr = message["Filters"]
        if filtersStr != "":
            #Construct filters list
            filtersList = [name.strip(" ") for name in filtersStr.split("|")]
            
            #Apply all filters 
            for filterDescription in filtersList:
                #Separate filter name from parameters
                filterName, filterParameters = self.ParseFilterDescription(filterDescription)
                
                #Find filter
                filterObject = self._filtersManager.FindFilterByName(filterName)
                if filterObject != None:
                    #Apply filter now
                    filterObject.ApplyFilterToMessage(message, filterParameters)
                elif filterName != "":
                    raise Exception("Cannot find appropriate filter: ", filterName)
            
        self._outputRouter.PassMessage(message)
        
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