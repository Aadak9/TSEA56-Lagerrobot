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
		nodes = client.recv(n)
		nodes = list(nodes)
		nodes = [nodes[i:i+2] for i in range(0, len(nodes), 2)]
		print(nodes)
		return lagerbredd, lagerhöjd, nodes
			
	except:
		print("slutet sket sig")
	
def update_path(client):
	lagerbredd, lagerbredd, nodes = receive_map_data(client)	
	målnoder = {1:[1]}
	nodnumber = 2
	for nod in nodes:
		målnoder[nodnumber] = nod
		nodnumber += 1
	print(målnoder)
		
		
	
