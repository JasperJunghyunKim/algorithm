import sys
sys_input = sys.stdin.readline

NUM_CIIIES = int(sys_input())
NUM_BUSES = int(sys_input())

graph = [[float('inf') for _ in range(NUM_CIIIES + 1)] for _ in range(NUM_CIIIES + 1)]
for i in range(NUM_CIIIES + 1):
    graph[i][i] = 0

for _ in range(NUM_BUSES):
    c_from, c_to, price = map(int, sys_input().split())
    if graph[c_from][c_to] == float('inf') or graph[c_from][c_to] > price:
        graph[c_from][c_to] = price

# Floyd-Warshall
for stopover in range(1, NUM_CIIIES + 1):
    for x in range(1, NUM_CIIIES + 1):
        for y in range(1, NUM_CIIIES + 1):
            graph[x][y] = min(graph[x][y], graph[x][stopover] + graph[stopover][y])

# print answer
for x in range(1, NUM_CIIIES + 1):
    for y in range(1, NUM_CIIIES + 1):
        print(graph[x][y] if graph[x][y] != float('inf') else 0, end=' ')
    print()