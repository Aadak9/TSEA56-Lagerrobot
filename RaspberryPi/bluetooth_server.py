import socket

def server_init():
	global s
	hostMACaddress = 'B8:27:EB:E9:12:27'
	port = 4
	size = 1024 #?
	s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
	s.bind((hostMACaddress, port))
	s.listen(1)

def recieve_data():
	try:
		client, address = s.accept()
		while 1:
			data = client.recv(size)
			if data:
				print(data)
				client.send(data) #Echo back to client
				return data
				
	except:
		print("Closing socket")
		client.close()
		s.close()
