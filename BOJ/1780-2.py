#
# 24-03-15
# T2
# T1 대비 개선사항 : 
# 1. 불필요하게 plain 여부를 확인할 필요 없이 -> pixel 전후 값을 비교하고, 다르면 바로 재귀
# 2. size = 1 일 때 바로 리턴하는 조건 추가
# 4456 ms -> 2624 ms
#
import sys
sys_input = sys.stdin.readline

n = int(sys_input().strip())

paper = []

for _ in range(n):
    paper.append(list(map(int, sys_input().split())))

num_paper = [0, 0, 0]

def recursive(start_row, start_col, size):
    global num_paper
    
    if size == 1:
        num_paper[paper[start_row][start_col]] += 1
        return
    
    for row in range(start_row, start_row + size):
        for col in range(start_col, start_col + size):
            if paper[start_row][start_col] != paper[row][col]:
                recursive(start_row, start_col, size//3)
                recursive(start_row, start_col + size//3, size//3)
                recursive(start_row, start_col + size//3 + size//3, size//3)
                recursive(start_row + size//3, start_col, size//3)
                recursive(start_row + size//3, start_col + size//3, size//3)
                recursive(start_row + size//3, start_col + size//3 + size//3, size//3)
                recursive(start_row + size//3 + size//3, start_col, size//3)
                recursive(start_row + size//3 + size//3, start_col + size//3, size//3)
                recursive(start_row + size//3 + size//3, start_col + size//3 + size//3, size//3)
                return

    num_paper[paper[start_row][start_col]] += 1
    return
        
        
recursive(0, 0, n)
print(num_paper[-1], num_paper[0], num_paper[1], sep="\n")

#
# 24-03-15
# T1
# 

import sys
sys_input = sys.stdin.readline

n = int(sys_input().strip())

paper = []

for _ in range(n):
    paper.append(list(map(int, sys_input().split())))

num_paper = [0, 0, 0]

def recursive(start_row, start_col, size):
    paper_number = paper[start_row][start_col]
    plain_paper = True
    global num_paper
    
    if size == 1:
        num_paper[paper_number] += 1
        return
    
    for row in range(start_row, start_row + size):
        for col in range(start_col, start_col + size):
            if paper[row][col] != paper_number:
                plain_paper = False
    
    if plain_paper:
        num_paper[paper_number] += 1
        return
    
    else:
        recursive(start_row, start_col, size//3)
        recursive(start_row, start_col + size//3, size//3)
        recursive(start_row, start_col + size//3 + size//3, size//3)
        recursive(start_row + size//3, start_col, size//3)
        recursive(start_row + size//3, start_col + size//3, size//3)
        recursive(start_row + size//3, start_col + size//3 + size//3, size//3)
        recursive(start_row + size//3 + size//3, start_col, size//3)
        recursive(start_row + size//3 + size//3, start_col + size//3, size//3)
        recursive(start_row + size//3 + size//3, start_col + size//3 + size//3, size//3)
        
recursive(0, 0, n)
print(num_paper[-1], num_paper[0], num_paper[1], sep="\n")