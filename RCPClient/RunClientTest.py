'''Created by Dmytro Konobrytskyi, 2012(C)'''
import time
from RCPClient.RCPClient import RCConnect, RCPrint

if __name__ == '__main__':
    RCConnect("tcp://127.0.0.1:55557")
    i = 0
    while True:
        message = "message {0}".format(i)
        RCPrint('<HR COLOR="0099FF">')
        RCPrint("NoNameStream")
        RCPrint(message, "strStream")
        RCPrint(i, "intStream")
        RCPrint(i/3.759, "floatStream")
        RCPrint(i/3.59, "floatStream", destinations="Win1")
        RCPrint(i/3.9, "floatStream", destinations="Win2")
        RCPrint(i/3.759, "floatStream", destinations="Win2, Win1")
        RCPrint([x*x for x in xrange(i-5, i+5)], "int1DStream")
        RCPrint([1/(0.7+x) for x in xrange(i-5, i+5)], "float1DStream")
        print "Sent: ", message
        i+=1
        time.sleep(1)