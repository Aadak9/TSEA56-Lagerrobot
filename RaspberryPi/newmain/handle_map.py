import bluetooth as bt
import fastest_way3 as fw
import fastest_way_hinder as fwh

global lagerbredd
global lagerhöjd
global målnoder


def receive_map_data(client):
	global lagerbredd
	global lagerhöjd
	try:
		data = client.recv(1).hex()
		if data == "70":
			lagerbredd = client.recv(1).hex()
			lagerhöjd = client.recv(1).hex()
			num_nodes = client.recv(1).hex()
		else:
			return
	except:
		print("Misslyckad dataöverföring av lagerinfo")
	
	try:
		n = int(num_nodes)
		nodes = b''
		while len(nodes) < n:
			data = client.recv(n-len(nodes))
			if not data:
				raise ConnectionError("Error noder")
			nodes += data
		nodes = list(nodes)
		nodes = [nodes[i:i+2] for i in range(0, len(nodes), 2)]
		return lagerbredd, lagerhöjd, nodes	
	except:
		print("Misslyckad dataöverföring noder")
	
	
def update_path(client):
	print("jag är i update_path")
	global målnoder
	global correct_path
	lagerbredd, lagerhöjd, nodes = receive_map_data(client)	
	målnoder = {1:[1]}
	nodnumber = 2
	for nod in nodes:
		målnoder[nodnumber] = nod
		nodnumber += 1
	print("jag ska nu kalla på fastest way")
	väg, nodeorder, correct_path = fw.fastest_way(int(lagerbredd), int(lagerhöjd), målnoder)
	print("jag har nu kört fastest way")
	return väg, nodeorder


def remove_goal_node(current_node, next_node):
	global målnoder
	for i in målnoder:
		if målnoder[i] == [current_node, next_node]:
			filtered_values = [v for v in målnoder.values() if v != [current_node, next_node]]
			new_målnoder = {j + 1: val for j, val in enumerate(filtered_values)}
		elif målnoder[i] == [next_node, current_node]:
			filtered_values = [v for v in målnoder.values() if v != [next_node, current_node]]
			new_målnoder = {j + 1: val for j, val in enumerate(filtered_values)}
     
	målnoder = new_målnoder
	return


def get_målnoder():
	global målnoder
	return målnoder
	
		
def update_path_obstacles(obstacles, målnoder_kvar):
	global lagerbredd
	global lagerhöjd
	global correct_path
	print(lagerbredd, lagerhöjd, målnoder_kvar, obstacles)
	nav_plan, nodeorder, correct_path = fwh.fastest_way_hinder(int(lagerbredd), int(lagerhöjd), målnoder_kvar, obstacles) #OBS, MÅLNODER KVAR SKA VA ETT DICTIONARY MED MÅL, INTE ALLA NODER
	
	return nav_plan, nodeorder
	
	
def get_goal_nodes(correctpath):
	goalnodes = []
	correctpath = correctpath[:-1]
	i = 0
	for value in correctpath:
		if value == "goal":
			goalnodes.append(correctpath[i-2])
			goalnodes.append(correctpath[i-1])
			print(goalnodes)
		else:
			pass
		i += 1
	return goalnodes
	
def send_map(nav_plan, client):
	global correct_path
	goals = get_goal_nodes(correct_path)
	plan = list(nav_plan)
	client.send((len(nav_plan) + len(goals)).to_bytes(1, 'big'))
	
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
			client.send(b'\x05') #nu kommer två noder
			client.send(goals[0].to_bytes(1, 'big'))
			client.send(goals[1].to_bytes(1, 'big'))
			goals = goals[2:]
			print("skickat plocka")
		elif value == "lämna":	
			client.send(b'\x06')
			print("skickat lämna")
		elif value == "höger":
			client.send(b'\x07')
			print("skickat höger")	  
	 
	return
	

			
			
	
