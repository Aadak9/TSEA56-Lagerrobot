import socket

def init_bluetooth():
	hostMACaddress = 'B8:27:EB:E9:12:27'
	port = 4
	size = 1024
	s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
	s.bind((hostMACaddress, port))
	s.listen(1)
	return s
