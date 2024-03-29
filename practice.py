graph = [[float('inf') for _ in range(NUM_V + 1)] for _ in range(NUM_V + 1)]
for i in range(NUM_V + 1):
    graph[i][i] = 0

for _ in range(NUM_E):
    v_from, v_to, price = map(int, sys_input().split())
    if graph[v_from][v_to] == float('inf') or graph[v_from][v_to] > price:
        graph[v_from][v_to] = price

# Floyd-Warshall
for stopover in range(1, NUM_V + 1):
    for x in range(1, NUM_V + 1):
        for y in range(1, NUM_V + 1):
            graph[x][y] = min(graph[x][y], graph[x][stopover] + graph[stopover][y])