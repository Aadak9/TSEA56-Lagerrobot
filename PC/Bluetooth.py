import socket

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


while 1:
    if(input("wat") == "w"):
        size = 1024
        bluetoothinit()
        sendbyte(0xFF)
        data = s.recv(size)
        print(data)



