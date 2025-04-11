import socket


def bluetoothinit():
    global s
    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

    try:
        s.connect(('B8:27:EB:E9:12:27', 4))

    except:
        print("koppling till raspberry misslyckades")
    
    return



#while 1:
#    data = input()
#    if(data == "w"):
#        s.send((1).to_bytes(1, 'big'))
#    elif(data == "a"):
#        s.send((2).to_bytes(1, 'big'))
#    elif(data == "t"):
#        s.send((3).to_bytes(1, 'big'))
#     elif(data == "stop"):
#        break

def sendbyte(byte):
    s.send(byte.to_bytes(1, 'big'))
    return