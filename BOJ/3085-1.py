import sys
n = int(sys.stdin.readline())
board = []

for _ in range(n):
    board.append(list(sys.stdin.readline().strip()))


def find_max():
    max_cnt = 1
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if board[i][j] == board[i][j+1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > max_cnt:
                max_cnt = cnt

    for j in range(n):
        cnt = 1
        for i in range(n-1):
            if board[i][j] == board[i+1][j]:
                cnt += 1
            else:
                cnt = 1
            if cnt > max_cnt:
                max_cnt = cnt
    return max_cnt
    
max_cnt = 1

for i in range(n):
    for j in range(n):
        if i < n - 1 and board[i][j] != board[i+1][j]:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            max_cnt = max(max_cnt, find_max())
            board[i+1][j], board[i][j] = board[i][j], board[i+1][j]
        if j < n - 1 and board[i][j] != board[i][j+1]:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            max_cnt = max(max_cnt, find_max())
            board[i][j+1], board[i][j] = board[i][j], board[i][j+1]

print(max_cnt)