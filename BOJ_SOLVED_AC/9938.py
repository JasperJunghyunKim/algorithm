import sys
sys_input = sys.stdin.readline

num_bottles, num_drawers = map(int, sys_input().split(' '))

# INIT
max_bottles = [1 for _ in range(num_drawers + 1)]
cur_bottles = [0 for _ in range(num_drawers + 1)]
drawer = [i for i in range(num_drawers + 1)]
drawer_candid = [tuple(map(int, sys_input().split(' '))) for _ in range(num_bottles)]


def find(x):
    if drawer[x] == x:
        return x
    drawer[x] = find(drawer[x])
    return drawer[x]

def union(x, y):
    x = find(x)
    y = find(y)
    drawer[y] = x # make x root
    return

# a, b 가 각각의 disjoint set 을 연결할 수 있는 가교리고 생각
for i in range(num_bottles):
    a, b = drawer_candid[i]
    # 두 서랍이 '같은' set 일 경우
    if find(a) == find(b):
        if cur_bottles[find(a)] < max_bottles[find(a)]:
            cur_bottles[find(a)] += 1
            print('LADICA')
            continue
        else:
            print('SMECE')
            continue
    # 두 서랍이 '다른' set 일 경우
    else:
        if cur_bottles[find(a)] + cur_bottles[find(b)] < max_bottles[find(a)] + max_bottles[find(b)]:
            union(a, b)
            max_bottles[find(a)] += max_bottles[find(b)]
            cur_bottles[find(a)] += (cur_bottles[find(b)] + 1)
            print('LADICA')
            continue
        else:
            print('SMECE')
            continue