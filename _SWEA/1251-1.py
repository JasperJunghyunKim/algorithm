import sys
import math
sys_input = sys.stdin.readline
sys.setrecursionlimit(2000)

NUM_TC = int(sys_input().strip())
NUM_ISLANDS = 0
TAX = 0
depth = None

# Path Compression
def find(r, c):
    if root[(r,c)] == (r,c):
        return (r,c)
    # root[(r,c)] = find(r, c)
    return find(*root[(r,c)])

# Union By Rank
def union(r1,c1,r2,c2):
    r1, c1 = find(r1, c1)
    r2, c2 = find(r2, c2)
    if (r1, c1) == (r2, c2):
        return False
    if depth[(r1, c1)] > depth[(r2, c2)]:
        root[(r2, c2)] = (r1, c1)
    elif depth[(r1, c1)] < depth[(r2, c2)]:
        root[(r1, c1)] = (r2, c2)
    else:
        depth[(r2, c2)] += 1
        root[(r1, c1)] = (r2, c2)
    return True


for tc in range(1, NUM_TC + 1):
    NUM_ISLANDS = int(sys_input().strip())
    islands_r = list(map(int, sys_input().strip().split()))
    islands_c = list(map(int, sys_input().strip().split()))
    TAX = float(sys_input().strip())
    
    tunnels = []
    # find distance between all two different islands
    for i in range(NUM_ISLANDS):
        for j in range(i + 1, NUM_ISLANDS):
            len_tunnel = math.sqrt((islands_r[i] - islands_r[j]) ** 2 + (islands_c[i] - islands_c[j]) ** 2)
            tunnels.append((len_tunnel, islands_r[i], islands_c[i], islands_r[j], islands_c[j]))
    
    # sort ASC
    tunnels.sort(key = lambda x : (x[0]))
    
    # make set
    root = {(islands_r[i], islands_c[i]): (islands_r[i], islands_c[i]) for i in range(NUM_ISLANDS)}
    depth = {(islands_r[i], islands_c[i]): 0 for i in range(NUM_ISLANDS)}
    
    # from shortest tunnel to longest tunnel
    num_tunnels_established = 0
    total_tax = 0
    for d, r1, c1, r2, c2 in tunnels:
        # all connected
        if num_tunnels_established == NUM_ISLANDS - 1:
            break
        can_establish = union(r1, c1, r2, c2)
        if can_establish:
            num_tunnels_established += 1
            total_tax += (TAX * (d ** 2))
    print("#" + str(tc), math.floor(total_tax + 0.5))