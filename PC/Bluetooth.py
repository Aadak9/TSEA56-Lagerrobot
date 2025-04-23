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
    data = s.recv(size)
    return data[0]

#bluetoothinit()
#time.sleep(1)
<<<<<<< HEAD
#size = 1024

#while True:
#  sendbyte(0x00)
#  data = s.recv(size)
#  print(data)
=======
size = 1024

#while 1:
#sendbyte(0x00)
#data1 = s.recv(size)
#print(data1[0])
#  sendbyte(0x01)
#  data2 = s.recv(size)
#  print(data2)
#  sendbyte(0x02)
#  data3 = s.recv(size)
#  print(data3)
>>>>>>> 32ea9b0fc08394eba68b66096849f79e459a9c41
  



