import spidev



def active_mode():
	try:
		client, address = s.accept()
		
		while True:
			try:
				data = client.recv(size)
				if not data:
					client.close()
					break 
					
				else:
					info = data[0]
					
					if info = 0x40:
						Automatic = True
						return Automatic
						
					elif info = 0x41:
						Automatic = False
						return Automatic
					else:
						continue
			
			except:
				break
	
	except Exception as e:
		print("Disconnected, looking for new socket", e)
							
						
							
					
