'''Created by Dmytro Konobrytskyi, 2012(C)'''

import numpy as num
import wx

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
from numpy import arange, sin, pi

class GraphPanel(wx.Panel):
    def __init__(self, parent, streamValuesHistory):
        wx.Panel.__init__(self, parent)
        self._streamValuesHistory = streamValuesHistory

        self.figure = Figure()
        self.figure.patch.set_facecolor('black')
        self.axes = self.figure.add_axes([0.1, 0.025, 0.9, 0.95])

        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()
        
        self._colors = [(0.0, 1.0, 0.0), (1.0, 0.0, 0.0), (0.0, 0.0, 1.0), (1.0, 1.0, 0.0), (1.0, 0.0, 1.0), (0.0, 1.0, 1.0)]

    def UpdateGraphs(self):
        self.axes.clear()
        self.axes.patch.set_facecolor((0, 0, 0))
        self.axes.grid(b=True, color=(0, 0.1, 0), which='major', linestyle='-', linewidth=1)
        self.axes.yaxis.set_tick_params(labelcolor=(0.6, 0.6, 0.6))

        """Draw data."""
        iColor = 0
        for streamValues in self._streamValuesHistory.itervalues():
            valuesNumber = int(self.axes.get_window_extent().width) / 4
            X = range(0, valuesNumber)
            Y = [streamValues[-min(valuesNumber, len(streamValues))]] * (valuesNumber - len(streamValues)) + streamValues[-valuesNumber:]
            self.axes.plot( X, Y, color=self._colors[iColor], linewidth=1)
            iColor+=1
            
        self.canvas.draw()

from RCPServer.MessageDestination.DestinationBase import DestinationBase
class GraphsWindow(DestinationBase, wx.Frame):
    '''
    This destination class shows a list of streams and their values
    '''
    def __init__(self, windowName):
        if windowName == "": 
            windowName = "Default console" #No name destination is default console
        wx.Frame.__init__(self, None, title=windowName)

        self._streamValuesHistory = {}        
        self._streamValues = {}
        self._graph = GraphPanel(self, self._streamValuesHistory)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self._graph, 1, wx.EXPAND)
        self.SetSizer(sizer)
        
        #Run graph updating timer
        timerOwner = wx.EvtHandler()
        self._mainTimer = wx.Timer(timerOwner, wx.ID_ANY)
        self._mainTimer.Start(500)
        timerOwner.Bind(wx.EVT_TIMER, self.UpdateGraphData, self._mainTimer)

    def UpdateGraphData(self, event):
        for streamName in self._streamValues.iterkeys():
            #Create new hostiry list if it's not created yet
            if streamName not in self._streamValuesHistory:
                self._streamValuesHistory[streamName] = []
            #Add new value to the history for a current stream
            streamHistory = self._streamValuesHistory[streamName]
            streamHistory.append(self._streamValues[streamName])
        
        #Update graph window
        self._graph.UpdateGraphs()
        
    def ProcessMessage(self, newMessage):
        #Update current stream values
        self._streamValues[newMessage["StreamName"]] = newMessage["Value"]
