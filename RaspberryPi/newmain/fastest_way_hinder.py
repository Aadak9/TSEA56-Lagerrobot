from collections import deque
import itertools
#Får lagerbredd, lagerhöjd, koordinater för målnod från PC

def skapa_graf(lagerbredd, lagerhöjd):
    #skapar dictionary med alla grannar nedåt och till höger för alla noder i lagret
    graf = {}
    nx = lagerbredd + 1
    ny = lagerhöjd + 1
    for y in range(ny):
        for x in range(nx):
            node = y * nx + x + 1
            graf[node] = []
            # höger granne
            if x < nx - 1:
                graf[node].append(node + 1)
            # nedåt granne
            if y < ny - 1:
                graf[node].append(node + nx)
            # vänster granne
            if x > 0:
                graf[node].append(node - 1)
            # övre granne
            if y > 0:
                graf[node].append(node-nx)
    return graf

def bfs(graf, startnod, målnod, last_node):
    
    paths = [] 
    for i  in range(len(startnod)):
        queue = deque([[startnod[i]]])
        visited = set()
        while queue:
            path = queue.popleft()
            node = path[-1]
            if node in visited:
                continue
            visited.add(node)
            for neighbor in graf[node]:
                new_path = path + [neighbor]
                if [node, neighbor] == målnod or [neighbor, node] == målnod or [neighbor] == målnod:
                    paths.append(new_path + ['goal'])
                queue.append(new_path)
    if len(paths) == 2:
        return min(paths, key=len)
    if last_node == 0:
        return min(paths, key=len)
    for i in paths[:]:
        if i[0] == last_node:
            paths.remove(i)
    return min(paths, key=len)
    #skriv om så att den bara tar bort om sträckan är lika lång från båda närliggande noder.

    
def skapa_avståndsmatris(graf, nodes):
    ant_noder  = len(nodes) 
    matris = [[0]*ant_noder for _ in range(ant_noder)]
    for i in range(ant_noder):
        for j in range(ant_noder):
            if i != j:
                path = bfs(graf, nodes[i+1], nodes[j+1], 0)
                if i == 0:
                    matris[i][j] = len(path) - 2 if path else float('infinity')
                else:
                    matris[i][j] = len(path) - 1 if path else float('infinity')

    
    return matris
 
def held_karp_väg(matris, start_index=0, end_index=None):
    n = len(matris)
    if end_index is None:
        end_index = n - 1  # standard: sista nod

    dp = [[float('inf')] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]
    dp[1 << start_index][start_index] = 0  # Startar i start_index

    for mask in range(1 << n):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v) or v == start_index:
                    continue
                next_mask = mask | (1 << v)
                new_cost = dp[mask][u] + matris[u][v]
                if new_cost < dp[next_mask][v]:
                    dp[next_mask][v] = new_cost
                    parent[next_mask][v] = u

    # Avsluta i end_index, inte tillbaka till start
    full_mask = (1 << n) - 1
    slutkostnad = dp[full_mask][end_index]
    current = end_index
    path = []

    # Återskapa vägen baklänges
    mask = full_mask
    while current != -1:
        path.append(current)
        prev = parent[mask][current]
        mask = mask ^ (1 << current)
        current = prev

    path = list(reversed(path))
    return slutkostnad, path


def node_to_xy(node, lagerbredd, lagerhöjd):
    nx = lagerbredd + 1
    ny = lagerhöjd + 1
    for i in range(0, nx):
        for j in range(0, ny):
            if node == j + ny * i + 1:
                return(i, j)
            else:
                continue
    
    return(0,0)
            

def get_direction(p1, p2):
    return (p2[0] - p1[0], p2[1] - p1[1])

def direction_to_angle(direction):
    # Gör om (dx, dy) till en riktning i grader
    if direction == (0, 1):
        return 0    # nedåt
    elif direction == (1, 0):
        return 90   # höger
    elif direction == (0, -1):
        return 180  # uppåt
    elif direction == (-1, 0):
        return 270  # vänster
    else:
        return None # ogiltig

def sväng_instructions(correct_path, lagerbredd, lagerhöjd, hinder):
    directions = []
    # Ta bort 'goal'
    pos = [node_to_xy(n, lagerbredd, lagerhöjd) for n in correct_path if isinstance(n, int)]
    if len(pos) < 2:
        return directions

    # Start: initial riktning
    if hinder[-1][0] == correct_path[0]:
        prev_dir = get_direction(node_to_xy(hinder[-1][1], lagerbredd, lagerhöjd),node_to_xy(hinder[-1][0], lagerbredd, lagerhöjd))
        prev_angle = direction_to_angle(prev_dir)
    elif hinder[-1][1] == correct_path[0]:
        prev_dir = get_direction(node_to_xy(hinder[-1][0], lagerbredd, lagerhöjd),node_to_xy(hinder[-1][1], lagerbredd, lagerhöjd))
        prev_angle = direction_to_angle(prev_dir)
   
    
    for i in range(0, len(pos)-1):
        #print(correct_path[i])
        current_dir = get_direction(pos[i], pos[i+1])
        #print("curr dir" + str(current_dir))    
        current_angle = direction_to_angle(current_dir)
        #print("curr angle" + str(current_angle))

        if prev_angle is None or current_angle is None:
            directions.append("plocka")  # vändning vid oklar rörelse
        else:
            delta = (current_angle - prev_angle) % 360
            #print("delta " + str(delta))
            if delta == 0:
                directions.append("rakt")  # rakt fram
            elif delta == 90:
                directions.append("vänster")  # höger
            elif delta == 270:
                directions.append("höger")  # vänster
            elif delta == 180:
                directions.append("vänd")  # vändning
            else:
                directions.append("vänd")  # vändning

            prev_angle = current_angle
    
    if current_angle == 270:
        directions.append("höger")
    elif current_angle == 180:
        directions.append("rakt")


    return directions

def remove_path(Graf, n1, n2):
    #ta bort n1 från n2´s grannar och n2 från n1´s grannar
    for i in Graf:
        if i == n1:
            Graf[i].remove(n2)
        elif i == n2:
            Graf[i].remove(n1)
    
    return(Graf)
            

def fastest_way_hinder(lagerbredd, lagerhöjd, målnoder, hinder):
	
    key = list(målnoder)[-1]
    if målnoder[key] != [1]:
	    målnoder[len(målnoder)+1] = [1] #ska alltid avsluta i nod 1
	    
    Graf = skapa_graf(lagerhöjd, lagerbredd) # skapa fullständig graf
    for i in hinder:
        Graf = remove_path(Graf, i[0], i[1]) #ta bort varje hinder, sista i listan är sist påkommna hindret

    matris = skapa_avståndsmatris(Graf, målnoder)

    kostnad, ordning = held_karp_väg(matris, start_index=0, end_index=(len(målnoder)-1))


    path = []
    #beräkna vägen till alla varor
    for i in range(len(ordning)-1):
        if len(path) > 0: 
            last_path = path[i-1]
            path.append(bfs(Graf, målnoder[ordning[i] + 1], målnoder[ordning[i+1] + 1], last_path[-3]))
        else:
            path.append(bfs(Graf, målnoder[ordning[i] + 1], målnoder[ordning[i+1] + 1], 0))

    correct_path = [item for sublist in path for item in sublist]
    
    nodeorder = []
    for i in correct_path:
        if isinstance(i,int):
            nodeorder.append(i)

    väg = deque(sväng_instructions(correct_path, lagerbredd, lagerhöjd, hinder))
    
    if väg[-1] != "lämna" :
        väg.append("lämna")

    return väg, nodeorder



#fastest_way_hinder(4, 3, {1:[20], 2:[14,18], 3:[13,17], 4:[4,8]}, [[3,7], [11,12], [18,19], [9,13], [16,20]])
#bredd, höjd, dictionary med målnoder där första är startnod och resterande är plockstationer, lista med hinder där sista är sist påkomna hindret
