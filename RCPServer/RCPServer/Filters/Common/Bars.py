'''Created by Dmytro Konobrytskyi, 2012(C)'''
from RCPServer.Filters.FilterBase import FilterBase

import matplotlib.pyplot
from RCPServer.Filters.ImagesStorage import ImagesStorage

class Bars(FilterBase):
    '''
    This filter creates a figure with vertical or horizontal 
    bars based on an input values array. 
    '''

    def __init__(self):
        #Call default parent constructor
        FilterBase.__init__(self)

    def ConstructDefaultParameters(self):
        return {"direction":"V", "width":"4", "height":"2", "dpi":"30"}
        
    def ApplyFilter(self, message, filterParameters):
        print message["Value"]
        values = [float(v) for v in str(message["Value"])[1:-1].split(", ")]
        pos = [float(y)+0.5 for y in range(len(values))]
        
        fig = matplotlib.pyplot.figure(figsize=(float(filterParameters["width"]), float(filterParameters["height"])), dpi=float(filterParameters["dpi"]))
        ax=fig.add_subplot(111)

        if filterParameters["direction"] == "H":
            ax.barh(pos, values, align='center')
        else:
            ax.bar(pos, values, align='center')
        
        #Use stream name as a title
        ax.set_title(message["StreamName"])
        #We need to delete stream name to don't have it in the output
        message["StreamName"] = None
        
        message["Value"] = '<img align="left" src="memory:%s"><br>'%ImagesStorage.AddFigure(fig)
        