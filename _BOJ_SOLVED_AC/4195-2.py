import sys
sys_input = sys.stdin.readline

def find(name):
    if name not in network:
        network[name] = name
        size_network[name] = 1
        depth_network[name] = 0
    if network[name] == name:
        return name
    network[name] = find(network[name])
    return network[name]

def union(name_a, name_b):
    root_a = find(name_a)
    root_b = find(name_b)
    if root_a == root_b:
        return
    if depth_network[root_a] > depth_network[root_b]:
        network[root_b] = root_a
        size_network[root_a] += size_network[root_b]
    elif depth_network[root_a] < depth_network[root_b]:
        network[root_a] = root_b
        size_network[root_b] += size_network[root_a]
    else:
        network[root_b] = root_a
        size_network[root_a] += size_network[root_b]
        depth_network[root_a] += 1
        

NUM_TC = int(sys_input().strip())
for _ in range(NUM_TC):
    network = {}
    size_network = {}
    depth_network = {}
    for _ in range(int(sys_input().strip())):
        name_a, name_b = sys_input().strip().split()
        union(name_a, name_b)
        print(size_network[find(name_a)])