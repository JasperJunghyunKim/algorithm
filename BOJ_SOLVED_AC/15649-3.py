N, M = map(int, input().split())

stack = []
visited = [False for _ in range(N + 1)]

def recursive(n):
    if len(stack) == M:
        print(*stack, sep=" ")
    else:
        for i in range(1, N + 1):
            if visited[i] == False:
                stack.append(i)
                visited[i] = True
                recursive(i)
                stack.pop()
                visited[i] = False
                
for i in range(1, N + 1):
    stack.append(i)
    visited[i] = True
    recursive(i)
    stack.pop()
    visited[i] = False