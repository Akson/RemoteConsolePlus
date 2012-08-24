'''Created by Dmytro Konobrytskyi, 2012(C)'''
import time
from RCPClient.RCPClient import RCConnect, RCPrint

if __name__ == '__main__':
    RCConnect("tcp://127.0.0.1:55557")
    i = 0
    while True:
        message = "message {0}".format(i)
        RCPrint(message)
        RCPrint(i)
        RCPrint(i/3.759)
        print "Sent: ", message
        i+=1
        time.sleep(1)