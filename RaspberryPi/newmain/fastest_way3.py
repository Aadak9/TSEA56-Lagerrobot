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
 
def held_karp_väg(matris):
    n = len(matris)
    dp = [[float('inf')] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]
    dp[1][0] = 0  # Startar i nod 0

    for mask in range(1 << n):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v):
                    continue
                next_mask = mask | (1 << v)
                new_cost = dp[mask][u] + matris[u][v]
                if new_cost < dp[next_mask][v]:
                    dp[next_mask][v] = new_cost
                    parent[next_mask][v] = u

    # Hitta bästa retur till start
    slutkostnad = float('inf')
    sista_nod = -1
    full_mask = (1 << n) - 1
    for i in range(1, n):
        cost = dp[full_mask][i] + matris[i][0]
        if cost < slutkostnad:
            slutkostnad = cost
            sista_nod = i

    # Återskapa vägen baklänges
    path = [0]
    mask = full_mask
    current = sista_nod
    while current != -1:
        path.append(current)
        prev = parent[mask][current]
        mask = mask ^ (1 << current)
        current = prev

    path = list(reversed(path))
    return slutkostnad, path

def node_to_xy(node, lagerbredd):
    nx = lagerbredd + 1
    x = (node - 1) % nx
    y = (node - 1) // nx
    return (x, y)

def get_direction(p1, p2):
    return (p2[0] - p1[0], p2[1] - p1[1])

def direction_to_angle(direction):
    # Gör om (dx, dy) till en riktning i grader
    if direction == (1, 0):
        return 0    # nedåt
    elif direction == (0, 1):
        return 90   # höger
    elif direction == (-1, 0):
        return 180  # uppåt
    elif direction == (0, -1):
        return 270  # vänster
    else:
        return None # ogiltig

def sväng_instructions(correct_path, lagerbredd):
    directions = []
    # Ta bort 'goal' om den finns
    pos = [node_to_xy(n, lagerbredd) for n in correct_path if isinstance(n, int)]
    #print(pos)
    if len(pos) < 2:
        return directions

    # Start: initial riktning
    prev_angle = 0
    #print("dir" + str(prev_dir))
    #print("angle" + str(prev_angle))
    
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
                directions.append("vänd")  # fallback, vändning

            prev_angle = current_angle
        
    if current_angle == 270:
        directions.append("höger")
    elif current_angle == 180:
        directions.append("rakt")


        #print("priv angle " + str(prev_angle))


    return directions

Graf = skapa_graf(3, 3)
målnoder = {1:[1], 2:[13,14], 3:[10,14], 4:[14,15]} #noder som ska besökas, där första noden är start och slutnod
matris = skapa_avståndsmatris(Graf, målnoder)
kostnad, ordning = held_karp_väg(matris)

path = []
#beräkna vägen till alla varor
for i in range(len(ordning)-1):
    if len(path) > 0: 
        last_path = path[i-1]
        path.append(bfs(Graf, målnoder[ordning[i] + 1], målnoder[ordning[i+1] + 1], last_path[-3]))
    else:
        path.append(bfs(Graf, målnoder[ordning[i] + 1], målnoder[ordning[i+1] + 1], 0))

correct_path = [item for sublist in path for item in sublist]

print(correct_path)
print(kostnad)

print(sväng_instructions(correct_path, 3))