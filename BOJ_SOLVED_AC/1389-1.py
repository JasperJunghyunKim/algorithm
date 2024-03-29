import sys
sys_input = sys.stdin.readline

NUM_USR, NUM_REL = map(int, sys_input().split())
adj_matrix = [[float('inf') for _ in range(NUM_USR + 1)] for _ in range(NUM_USR + 1)]

for i in range(NUM_USR + 1):
    adj_matrix[i][i] = 0

for _ in range(NUM_REL):
    user_from, user_to = map(int, sys_input().split())
    adj_matrix[user_from][user_to] = 1
    adj_matrix[user_to][user_from] = 1

for i in range(1, NUM_USR + 1):
    for a in range(1, NUM_USR + 1):
            for b in range(1, NUM_USR + 1):
                adj_matrix[a][b] = min(adj_matrix[a][b], adj_matrix[a][i] + adj_matrix[i][b])

kevinbacon = [sum(i[1:]) for i in adj_matrix]
print(kevinbacon.index(min(kevinbacon)))