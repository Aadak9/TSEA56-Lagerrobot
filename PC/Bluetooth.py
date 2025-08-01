import socket
import time
import threading

bluetoothlock = threading.Lock()

def bluetoothinit():
    global s
    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    #s.settimeout(1)
    try:
        s.connect(('B8:27:EB:E9:12:27', 4))
        print("Ansluten till raspberry pi")

    except:
        print("koppling till raspberry misslyckades")
    
    return

def sendbyte(byte):
    try:
        #print(byte)
        s.send(byte.to_bytes(1, 'big'))  # Skicka 1 byte
    except Exception as e:
        print(f"Fel vid sändning av byte: {e}")



def receive_data(size):
    try:
        data = s.recv(size)  # Vänta på att ta emot 1 byte
        if data:
            if len(data) == 1:
                return data[0]
            else:
                return data 
    except Exception as e:
        print(f"Fel vid mottagning av data: {e}")
    return None
  

def send_and_receive(command):
    #with bluetoothlock:
    try:
        sendbyte(command)
        received = receive_data(1)
        return received
    except Exception as e:
        print(f"knas med {e}")
        return




