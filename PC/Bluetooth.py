import socket
import time

def bluetoothinit():
    global s
    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

    try:
        s.connect(('B8:27:EB:E9:12:27', 4))
        print("Ansluten till raspberry pi")

    except:
        print("koppling till raspberry misslyckades")
    
    return

def sendbyte(byte):
    s.send(byte.to_bytes(1, 'big'))
    return

bluetoothinit()
time.sleep(1)
size = 1024

while True:
  sendbyte(0x00)
  data = s.recv(size)
  print(data)
  



