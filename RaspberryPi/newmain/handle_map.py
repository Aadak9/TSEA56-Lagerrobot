import bluetooth as bt
import fastest_way3 as fw




def receive_map_data(client):
	try:
		data = client.recv(1).hex()
		if data == "70":
			lagerbredd = client.recv(1).hex()
			lagerhöjd = client.recv(1).hex()
			num_nodes = client.recv(1).hex()
			print(lagerbredd, lagerhöjd, num_nodes)
		else:
			return
	except:
		print("början sket sig")
	
	
	try:
		print(num_nodes)
		n = int(num_nodes)
		nodes = b''
		while len(nodes) < n:
			data = client.recv(n-len(nodes))
			if not data:
				raise ConnectionError("misslyckat dataöverföring noder")
			nodes += data
		nodes = list(nodes)
		nodes = [nodes[i:i+2] for i in range(0, len(nodes), 2)]
		print(nodes)
		return lagerbredd, lagerhöjd, nodes
			
	except:
		print("slutet sket sig")
	
def update_path(client):
	lagerbredd, lagerhöjd, nodes = receive_map_data(client)	
	målnoder = {1:[1]}
	nodnumber = 2
	for nod in nodes:
		målnoder[nodnumber] = nod
		nodnumber += 1
	
	väg = fw.fastest_way(int(lagerbredd), int(lagerhöjd), målnoder)
	return väg	
		
	
def send_map(nav_plan, client):
	plan = list(nav_plan)
	print(len(plan))
	client.send(len(plan).to_bytes(1, 'big'))
	for value in plan:

		if value == "vänster":
			client.send(b'\x02')
			print("skickat vänster")
		elif value == "rakt":
			client.send(b'\x03')
			print("skickat rakt")
		elif value == "vänd":
			client.send(b'\x04')
			print("skickat vänd")
		elif value == "plocka":	
			client.send(b'\x05')
			print("skickat plocka")
		elif value == "lämna":	
			client.send(b'\x06')
			print("skickat lämna")
		elif value == "höger":
			client.send(b'\x07')
			print("skickat höger")
	return
			
		
			
		
	
