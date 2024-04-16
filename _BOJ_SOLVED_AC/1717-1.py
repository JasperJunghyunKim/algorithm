########################################
# T2 : Compare Tree Depth
# Union 할 때 Tree Depth 비교
########################################
import sys
sys_input = sys.stdin.readline
n, commands = map(int, sys_input().split(' '))
sys.setrecursionlimit(1_000_000)

# INIT
set_1717 = [i for i in range(0, n+1)]
depth_set_1718 = [0 for _ in range(0, n+1)]

def find(x):
    if set_1717[x] == x:
        return x
    return find(set_1717[x])

def union(x,y):
    x = find(x)
    y = find(y)
    if x ==y:
        return
    if depth_set_1718[x] > depth_set_1718[y]:
        set_1717[y] = x
    elif depth_set_1718[y] > depth_set_1718[x]:
        set_1717[x] = y
    else:
        set_1717[y] = x
        depth_set_1718[x] += 1
    return

def is_set(x, y):
    if find(x) == find(y):
        return 'YES'
    else:
        return 'NO'
    
for _ in range(commands):
    cmd, x, y = map(int, sys_input().split(' '))
    if cmd == 0:
        union(x, y) 
    elif cmd == 1:
        print(is_set(x,y))

########################################
# T1 : Path Compression
# find 할 때 root 를 변경
########################################
import sys
sys_input = sys.stdin.readline
n, commands = map(int, sys_input().split(' '))
sys.setrecursionlimit(1_000_000)

# INIT
set_1717 = [i for i in range(0, n+1)]

# FUNC
def find(x):
    if set_1717[x] == x:
        return x
    set_1717[x] = find(set_1717[x])
    return set_1717[x]

def union(x, y):
    x = find(x)
    y = find(y)
    set_1717[x] = y

def is_set(x, y):
    if find(x) == find(y):
        return 'YES'
    else:
        return 'NO'
    
for _ in range(commands):
    cmd, x, y = map(int, sys_input().split(' '))
    if cmd == 0:
        union(x, y) 
    elif cmd == 1:
        print(is_set(x,y))