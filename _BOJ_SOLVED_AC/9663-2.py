#
# 24-03-28
# 
N = int(input())

# IDXth Row saves col number
row = [0] * (N + 1)
answer = [0]

def is_promising(nxt_row, nxt_col):
    for prev_row in range(1, nxt_row):
        if row[prev_row] == nxt_col or abs(nxt_col - row[prev_row]) == nxt_row - prev_row:
            return False
    return True

def recursive(cur_row):
    if cur_row == N:
        answer[0] += 1
        return
    for nxt_col in range(1, N + 1):
        if is_promising(cur_row + 1, nxt_col):
            row[cur_row + 1] = nxt_col
            recursive(cur_row + 1)
            row[cur_row + 1] = 0

recursive(0)


print(answer[0])