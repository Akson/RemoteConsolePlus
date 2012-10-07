'''Created by Dmytro Konobrytskyi, 2012(C)'''
import wx
from Network.ZMQServer import ZMQServer
from UI.UIManager import UIManager
from MessageProtocol.JSONWithBinaryTail import ProtocolParser
from ConfigManager.ConfigManager import NetworkConfig
from multiprocessing import Process, Pipe
from Router.InputRouter import InputRouter
from Router.OutputRouter import OutputRouter

class RCPCollectorProcess(Process):
    '''
    This is a process that receive messages from ZMQ, apply filters and send them to emmiter process through the pipe
    '''
    def __init__(self, pipe):
        Process.__init__(self)
        self._pipe = pipe  

    def run(self):
        #Close the output part of a pipe which we don't need since we are only sending data
        outputPipe, inputPipe = self._pipe
        outputPipe.close()

        #Create a collector pipeline
        server = ZMQServer()
        protocolParser = ProtocolParser()
        inputRouter = InputRouter(inputPipe)

        #Run a message loop. It continuously reads ZMQ messages, parses them, apply filters and send to the Emitter through the pipe
        while True:
            message = server.ReceiveMessages()
            message = protocolParser.ParseProtocolMessage(message)
            inputRouter.PassMessage(message)
            
class RCPServer(object):
    '''
    Main class of RCP server. It creates and controls all message processing pipeline components.
    '''

    def __init__(self):
        #Create a pipe for connecting Collector and Emitter
        pipe = Pipe()
        
        #Run a Collector process
        self._collectorProcess = RCPCollectorProcess(pipe)
        self._collectorProcess.daemon = True    #This means that when UI process ends it will kill the collector process
        self._collectorProcess.start()

        #Close this part of a pipe, since we don't send any data on this side
        outputPipe, inputPipe = pipe
        inputPipe.close()
        self._outputPipe = outputPipe 

        self._app = wx.App(redirect=False)  #default error output to console
        self._uiManager = UIManager()
        self._outputRouter = OutputRouter(self._uiManager)

        #Run main message receiving timer
        timerOwner = wx.EvtHandler()
        self._mainTimer = wx.Timer(timerOwner, wx.ID_ANY)
        self._mainTimer.Start(NetworkConfig.ReceivingMessagesInterval)
        timerOwner.Bind(wx.EVT_TIMER, self.ProcessMessagess, self._mainTimer)
        timerOwner.Bind(wx.EVT_IDLE, self.ProcessMessagess, self._mainTimer)
        
        self._app.MainLoop()

    def ProcessMessagess(self, event):
        #Read incoming messages
        incomingMessages = []
        while self._outputPipe.poll():
            try:
                message = self._outputPipe.recv()
            except IOError:
                #Collector has died, time to exit
                exit()
            incomingMessages.append(message)
        
        #Send incoming messages to destinations
        for message in incomingMessages:
            self._outputRouter.PassMessage(message)
