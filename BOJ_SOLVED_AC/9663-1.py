#
# 24-03-18
# 2차원 배열로 구현해보려고 했으나, 일단 구현부터 실패
# 다른 풀이 블로그를 참고해보았고, 1차원 배열으로 단순화하여 해결 예정
#

import sys
sys_input = sys.stdin.readline

n = int(sys_input().strip())

answer = [0]

def available(next_row, next_col):
    # (next_row, next_col) as a basis, check vertical, horizontal overlap positions
    for pos_row, pos_col in pos_queens:
        if pos_row == next_row or pos_col == next_col:
            return False
    
    # (next_row, next_col) as a basis, make diagonal options
    diagonal = []
    for i in range(0, n):
        diag_row, diag_col = next_row + i, next_row + i
        if 0 <= diag_row < n and 0 <= diag_col < n: diagonal.append((diag_row, diag_col))
        
        diag_row, diag_col = next_row + i, next_row - i
        if 0 <= diag_row < n and 0 <= diag_col < n: diagonal.append((diag_row, diag_col))
        
        diag_row, diag_col = next_row - i, next_row + i
        if 0 <= diag_row < n and 0 <= diag_col < n: diagonal.append((diag_row, diag_col))
        
        diag_row, diag_col = next_row - i, next_row - i
        if 0 <= diag_row < n and 0 <= diag_col < n: diagonal.append((diag_row, diag_col))
        
    # (next_row, next_col) as a basis, check diagonal overlap positions
    for pos_row, pos_col in pos_queens:
        if (pos_row, pos_col) in diagonal:
            return False
    
    # (next_row, next_col) is horizontally, vertically, diagonally free
    return True

# stack (row, col)
pos_queens = []

for i in range(n):
    pos_queens.append((0, i))

    while pos_queens:
        cur_depth = len(pos_queens)
        
        if cur_depth == n:
            answer[0] += 1
            pos_queens.pop()
        
        else:  
            for col in range(n):
                if available(next_row = cur_depth, next_col = col):
                    pos_queens.append((cur_depth, col))
            pos_queens.pop()
            
def recursive()