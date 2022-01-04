from boot import mac
from esp import espnow

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
e.send(peer,"From mypython test mc from:"'{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(*mac))
print("end of main")

   