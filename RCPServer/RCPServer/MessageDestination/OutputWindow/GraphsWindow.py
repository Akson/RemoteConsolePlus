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
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()

    def UpdateGraphs(self):
        """Draw data."""
        for streamValues in self._streamValuesHistory.itervalues():
            plot_pts = num.array( streamValues )
            self.axes.plot( plot_pts[:,0], plot_pts[:,1])
            
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
        self._mainTimer.Start(200)
        timerOwner.Bind(wx.EVT_TIMER, self.UpdateGraphData, self._mainTimer)

    def UpdateGraphData(self, event):
        for streamName in self._streamValues.iterkeys():
            #Create new hostiry list if it's not created yet
            if streamName not in self._streamValuesHistory:
                self._streamValuesHistory[streamName] = []
            #Add new value to the history for a current stream
            streamHistory = self._streamValuesHistory[streamName]
            streamHistory.append((len(streamHistory),self._streamValues[streamName]))
        
        #Update graph window
        self._graph.UpdateGraphs()
        self._graph.canvas.Refresh()
        
    def ProcessMessage(self, newMessage):
        #Update current stream values
        self._streamValues[newMessage["StreamName"]] = newMessage["Value"]
