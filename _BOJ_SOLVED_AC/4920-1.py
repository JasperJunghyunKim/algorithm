import sys
sys_input = sys.stdin.readline

tc = 1

one_by_four = [[(0,0), (0,1), (0,2), (0,3)]]
two_by_three = [
    [(0,1), (1,0), (1,1), (1,2)],
    [(0,0), (0,1), (0,2), (1,1)],
    [(0,0), (0,1), (1,1), (1,2)],
    [(0,0), (0,1), (0,2), (1,2)],
    [(0,0), (1,0), (1,1), (1,2)]]
three_by_two = [
    [(0,0), (1,0), (2,0), (1,1)],
    [(1,0), (0,1), (1,1), (2,1)],
    [(0,1), (1,1), (1,0), (2,0)],
    [(0,0), (0,1), (1,0), (2,0)],
    [(2,0), (0,1), (1,1), (2,1)]]
two_by_two = [[(0,0), (0,1), (1,0), (1,1)]]
four_by_one = [[(0,0), (1,0), (2,0), (3,0)]]
while True:
    N = int(sys_input().strip())
    if N == 0:
        break
    board = [list(map(int, sys_input().strip().split())) for _ in range(N)]
    max_value = -float('inf')
    # one by four
    for r in range(N):
        for c in range(N - 3):
            for tetris in one_by_four:
                tmp_sum = 0
                for dr, dc in tetris:
                    tmp_sum += board[r + dr][c + dc]
                max_value = tmp_sum if tmp_sum > max_value else max_value
    # two by three
    for r in range(N - 1):
        for c in range(N - 2):
            for tetris in two_by_three:
                tmp_sum = 0
                for dr, dc in tetris:
                    tmp_sum += board[r + dr][c + dc]
                max_value = tmp_sum if tmp_sum > max_value else max_value
    # three by two
    for r in range(N - 2):
        for c in range(N - 1):
            for tetris in three_by_two:
                tmp_sum = 0
                for dr, dc in tetris:
                    tmp_sum += board[r + dr][c + dc]
                max_value = tmp_sum if tmp_sum > max_value else max_value
    # two by two
    for r in range(N - 1):
        for c in range(N - 1):
            for tetris in two_by_two:
                tmp_sum = 0
                for dr, dc in tetris:
                    tmp_sum += board[r + dr][c + dc]
                max_value = tmp_sum if tmp_sum > max_value else max_value    
    # four by one
    for r in range(N - 3):
        for c in range(N):
            for tetris in four_by_one:
                tmp_sum = 0
                for dr, dc in tetris:
                    tmp_sum += board[r + dr][c + dc]
                max_value = tmp_sum if tmp_sum > max_value else max_value    
    print(str(tc) + ".", max_value)
    tc += 1