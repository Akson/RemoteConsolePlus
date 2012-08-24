'''Created by Dmytro Konobrytskyi, 2012(C)'''
from RCPClient.RCPClient import RCPClient
import time

if __name__ == '__main__':
    RCPClient.Connect("tcp://127.0.0.1:55557")
    i = 0
    while True:
        message = "message {0}".format(i)
        RCPClient.Print(message)
        RCPClient.Print(i)
        RCPClient.Print(i/3.759)
        print "Sent: ", message
        i+=1
        time.sleep(1)