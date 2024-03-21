#
# 24-03-12
# hanoi_large 의 일반항을 구하면 return 2**n - 1 으로 바로 계산할 수 있음 (이 부분 블로그 참조함) 
#

import sys
sys_input = sys.stdin.readline

num_stack = int(sys_input().strip())
count = 0

answer = []

visited = {1:1}

def change(fix, target):
    if fix == 1 and target == 2:
        return 3
    elif fix == 1 and target == 3:
        return 2
    elif fix == 2 and target == 1:
        return 3
    elif fix == 2 and target == 3:
        return 1
    elif fix == 3 and target == 1:
        return 2
    elif fix == 3 and target == 2:
        return 1
    
def hanoi_small(n, start, end):
    if n == 1:
        print(start, end)
    else:
        hanoi_small(n-1, start, change(start, end))
        hanoi_small(1, start, end)
        hanoi_small(n-1, change(end, start), end)

def hanoi_large(n, start, end):
    # if n not in visited:
    #     visited[n] = hanoi_large(n-1, start, change(start, end)) + hanoi_large(1, start, end) + hanoi_large(n-1, change(end, start), end)
    # return visited[n]
    return 2**n -1
        
        
print(hanoi_large(num_stack, 1, 3))
if num_stack <= 20:
    hanoi_small(num_stack, 1, 3)