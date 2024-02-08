import sys
sys_input = sys.stdin.readline
tc = int(sys_input())

def find(name):
    if network.get(name) == name:
        return name
    network.update({name : find(network.get(name))})
    return network.get(name)

def union(name1, name2):
    name1 = find(name1)
    name2 = find(name2)
    if name1 == name2: return
    network.update({name2: name1})
    size_network.update({name1: size_network.get(name1) + size_network.get(name2)})
    return

for _ in range(tc):
    num_relation = int(sys_input())
    network = dict()
    size_network = dict()
    for _ in range(num_relation):
        a, b = sys_input().strip().split(' ')
        if network.get(a) == None:
            network.update({a: a})
            size_network.update({a: 1})
        if network.get(b) == None:
            network.update({b: b})
            size_network.update({b: 1})
        union(a, b)
        print(size_network.get(find(a)))