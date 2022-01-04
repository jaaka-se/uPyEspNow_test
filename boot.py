# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import network
import time
from esp import espnow
#import webrepl
wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)
#wlan.config(channel=9)
global mac
mac=wlan.config('mac')
print(" ")
print("My mac is ="'{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(*mac))
print('network config:', wlan.ifconfig())
#print("channel=",wlan.config('channel'))
#webrepl.start()
gc.collect()
print("running in main")
peer = b'\xff\xff\xff\xff\xff\xff'
e = espnow.ESPNow()
psk=b'1234567890abcdef'
def recv_cb(e):
    print("in receive")
    print(e.irecv(0))
    print("end of receive")
    
# readbuffer 3*258,timeout 10s,on_receive-callback
e.init(774,10000,recv_cb)
#global mac
print("From mypython test mc from:"'{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(*mac))
e.send(peer,"From mypython test4711  mc from:"'{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(*mac))
print("end of main")
i = 0
while i < 15 :
    e.send(peer,"From mypython test {} mc from:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}".format(i,*mac))
    print("SENT: From mypython test {} mc from:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}".format(i,*mac))
    #time.sleep(10)
    print(e.irecv(10000))
    print("last")
    i=i+1
