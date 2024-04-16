#
# 24-03-28
# BackTracking
#

N, M = map(int, input().split())

stack = []
len_stack = [0]
visited = [False for _ in range(N + 1)]

def recursive(n):
    if len_stack[0] == M:
        print(*stack, sep=" ")
    else:
        for i in range(1, N + 1):
            if visited[i] == False:
                stack.append(i)
                len_stack[0] += 1
                visited[i] = True
                recursive(i)
                stack.pop()
                len_stack[0] -= 1
                visited[i] = False
                
for i in range(1, N + 1):
    stack.append(i)
    len_stack[0] += 1
    visited[i] = True
    recursive(i)
    stack.pop()
    len_stack[0] -= 1
    visited[i] = False
    
#
# 24-03-28
# Permutaions
#
import itertools

N, M = map(int, input().split())
perm = list(itertools.permutations(range(1, N + 1), M))
for i in perm:
    print(*i, sep=" ")