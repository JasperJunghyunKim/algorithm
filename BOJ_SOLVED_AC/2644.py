import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split(' '))
num_rel = int(input())
family = {v:[] for v in range(1, n+1)}
for _ in range(num_rel):
    dad, son = map(int, input().split(' '))
    family[dad].append(son)
    family[son].append(dad)

# find shortest from a to b
visited = [-1] * (n + 1)

def dfs(dad, count):
    visited[dad] = count
    for son in family[dad]:
        # if visited[son] == -1 or visited[son] > count + 1:
        if visited[son] == -1:
            dfs(son, count + 1)

dfs(a, 0)
if visited[b] == -1:
    print(-1)
else:
    print(visited[b])

########################################
