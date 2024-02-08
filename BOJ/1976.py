import sys
sys_input = sys.stdin.readline

num_cities = int(sys_input())   # 200
num_plans = int(sys_input())    # 1000
graph = [list(map(int, sys_input().split(' '))) for _ in range(num_cities)]
plan = list(map(int, sys_input().split(' ')))

# INIT
city_set = [i for i in range(num_cities + 1)]
# FIND
def find(x):
    if city_set[x] == x:
        return x
    city_set[x] = find(city_set[x])
    return city_set[x]
# UNION
def union(x, y):
    x = find(x)
    y = find(y)
    city_set[x] = y
    return

for i in range(num_cities):
    for j in range(i + 1):
        if graph[i][j] == 1:
            union(i+1, j+1)

result = set()
for i in plan:
    result.add(find(i))
if len(result) == 1:
    print('YES')
else:
    print('NO')