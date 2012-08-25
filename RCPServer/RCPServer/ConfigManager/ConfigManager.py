'''Created by Dmytro Konobrytskyi, 2012(C)'''

class NetworkConfig(object):
    NetworkAddress = 'tcp://*:55557'
    ProcessLastMessages = 100 
    
class HTMLConsoleConfig(object):
    ConsoleMessageBufferSize = 200
    
class MessageConfig(object):
    #We will use this message to have all fields in all messages
    DefaultMessageFields = {"Value":"", "TimeStamp":0, "StreamName":"", "Filters":"", "Destinations":"", "BinaryData":None}