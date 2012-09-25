'''Created by Dmytro Konobrytskyi, 2012(C)'''
import time
from RCPClient.RCPClient import RCConnect, RCPrint

if __name__ == '__main__':
    RCConnect("tcp://127.0.0.1:55557")
    i = 0
    while True:
        message = "message {0}".format(i)
        RCPrint('<HR COLOR="blue">')
        RCPrint("NoNameStream")
        RCPrint(message, "strStream")
        RCPrint(i, "intStream")
        RCPrint(i/3.759, "floatStream")
        RCPrint(i/3.59, "floatStream", destinations="Win1")
        RCPrint(i/3.9, "floatStream", destinations="Win1")
        RCPrint(i/3.759, "floatStream", destinations=", Win1")
        RCPrint([x*x for x in xrange(i-5, i+5)], "int1DStream")
        RCPrint([1/(0.7+x) for x in xrange(i-5, i+5)], "float1DStream")

        RCPrint(i/3.759, "time", destinations="WinTime", filters="Time")
        RCPrint(i*1000+i/3.759, "time", destinations="WinTime", filters="Time")
        RCPrint(i*1000+i/3.759, "time", destinations="WinTime", filters='Time(unit=s)')
        RCPrint(i*1000+i/3.759, "time", destinations="WinTime", filters='Time(unit=s)|Font(color=green)')
        RCPrint(i*1000+i/3.759, "time", destinations="WinTime", filters='Font(color=green)')
        RCPrint(i*1000+i/3.759, "time", destinations="WinTime", filters='Font')

        RCPrint([1/(1+x)+x for x in range(i%7, i%7+i%5+1)], "Image name", filters='Bars')
        RCPrint([1/(1+x)+x for x in range(i%7, i%7+i%5+1)], "Image name", filters='Bars(width=2, height=4)')
        RCPrint([1/(1+x)+x for x in range(i%7, i%7+i%5+1)], "Image name", filters='Bars(direction=H)')
        
        print "Sent: ", message
        i+=1
        time.sleep(1)