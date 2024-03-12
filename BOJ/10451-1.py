import sys
input = sys.stdin.readline

n = int(input())

# for i in range(n):
#     num_v = int(input())
#     v_to = [0,]
#     v_to.extend(list(map(int, input().strip().split(' '))))
#     visited = [False]*(num_v+1)
#     count = 0
#     for i in range(1, num_v + 1):
#         if visited[i] == False:
#             count += 1
#             v_start = i
#             while visited[v_start] == False:
#                 visited[v_start] = True
#                 v_start = v_to[v_start]
#         else:
#             continue
#     print(count)

# visited 체크때문에 시간초과
for i in range(n):
    num_v = int(input())
    v_to = [0,]
    v_to.extend(list(map(int, input().strip().split(' '))))
    visited = []
    count = 0
    for i in range(1, num_v + 1):
        if i not in visited:
            count += 1
            v_start = i
            while v_start not in visited:
                visited.append(v_start)
                v_start = v_to[v_start]
        else:
            continue
    print(count)