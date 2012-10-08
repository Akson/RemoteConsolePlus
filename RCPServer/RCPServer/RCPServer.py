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

        #Run wx.Window framework since it may be used in some filters
        self._app = wx.App(redirect=False)

        #Create a collector pipeline
        server = ZMQServer()
        protocolParser = ProtocolParser()
        inputRouter = InputRouter(inputPipe)

        #Run a message loop. It continuously reads ZMQ messages, parses them, apply filters and send to the Emitter through the pipe
        while True:
            message = server.ReceiveMessages()
            message = protocolParser.ParseProtocolMessage(message)
            inputRouter.PassMessage(message)
            
class RCPEmitterProcess(Process):
    '''
    This is a process takes filtered messages from the pipe and send them to destinations. UI event loop works in it as well
    '''
    def __init__(self, pipe):
        Process.__init__(self)
        self._pipe = pipe  

    def run(self):
        #Close this part of a pipe, since we don't send any data on this side
        outputPipe, inputPipe = self._pipe
        inputPipe.close()
        self._outputPipe = outputPipe 

        app = wx.App(redirect=False)  #default error output to console
        uiManager = UIManager()
        self._outputRouter = OutputRouter(uiManager)

        #Run main message receiving timer
        timerOwner = wx.EvtHandler()
        mainTimer = wx.Timer(timerOwner, wx.ID_ANY)
        mainTimer.Start(NetworkConfig.ReceivingMessagesInterval)
        timerOwner.Bind(wx.EVT_TIMER, self.ProcessMessagess, mainTimer)
        timerOwner.Bind(wx.EVT_IDLE, self.ProcessMessagess, mainTimer)
        
        app.MainLoop()

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
        #self._collectorProcess.run()
        
        #Run a Collector process
        self._emitterProcess = RCPEmitterProcess(pipe)
        self._emitterProcess.daemon = True    #This means that when UI process ends it will kill the collector process
        #self._emitterProcess.start()
        self._emitterProcess.run()



