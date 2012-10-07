'''Created by Dmytro Konobrytskyi, 2012(C)'''
import time
from RCPClient.RCPClient import RCConnect, RCPrint
from numpy.ma.core import sin, cos

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

        if i%5 == 0:
            RCPrint([1/(1+x)+x for x in range(i%7, i%7+i%5+1)], "Image name", filters='Bars')
            RCPrint([1/(1+x)+x for x in range(i%7, i%7+i%5+1)], "Image name", filters='Bars(width=2, height=4)')
            RCPrint([1/(1+x)+x for x in range(i%7, i%7+i%5+1)], "Image name", filters='Bars(direction=H)')

        RCPrint((i%7)*100/7, "Progress bar 1", destinations="ProgressWindow(ProgressWindow)")
        RCPrint((i%9)*100/8, "Progress bar 2", destinations="ProgressWindow(ProgressWindow)")
        RCPrint((i%9)*100/8, "Progress bar 2", destinations="ProgressWindow2(ProgressWindow)")

        RCPrint(i/3.59, "floatStream1", destinations="TestList1(ListWindow)")
        RCPrint(i/3.9, "floatStream2", destinations="TestList1(ListWindow)")
        RCPrint(message, "floatStream3", destinations="TestList1(ListWindow)")

        RCPrint(sin(i/3.1), "floatStream1", destinations="TestGraph1(GraphsWindow)")
        RCPrint(cos(i/1.9), "floatStream2", destinations="TestGraph1(GraphsWindow)")
        RCPrint(cos(i/5.2), "floatStream3", destinations="TestGraph1(GraphsWindow)")
        
        print "Sent: ", message
        i+=1
        time.sleep(1)