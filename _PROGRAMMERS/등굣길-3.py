def solution(m, n, puddles):
    graph = [[0] * (m) for _ in range(n)]
    graph[0][0] = 1
    for puddle in puddles:
        # if 0 <= puddle[1] - 1 < n and 0 <= puddle[0] - 1 < m:
        graph[puddle[1] - 1][puddle[0] - 1] = -1
    print(*graph, sep="\n")
    for r in range(n):
        for c in range(m):
            from_upper = 0
            from_left = 0
            if r == 0 and c == 0: continue
            if graph[r][c] == -1: continue
            if r - 1 >= 0 and graph[r - 1][c] != -1:
                from_upper = graph[r - 1][c]
            if c - 1 >= 0 and graph[r][c - 1] != -1:
                from_left = graph[r][c - 1]
            graph[r][c] = (from_upper + from_left) % 1_000_000_007
    return graph[n - 1][m - 1] % 1_000_000_007

print(solution(4, 3, [[1, 1], [2, 1], [1, 2], [3, 1]]))