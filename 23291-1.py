import sys
sys_input = sys.stdin.readline
from collections import deque

# 최소 어항에 1마리 씩 더하기
# 가장 왼쪽을 쌓기
# 될때까지 굴리기
# 조절하기
# 1단으로 재배열
# 절반씩 두 번 굴리기 (N/2, N/4)
# 조절하기
# 1단으로 재배열

NUM_CAGE, MAX_DIFF = map(int, sys_input().split())
cage_map = deque([list(map(int, sys_input().split()))])

def organize():
    global cage_map
    # 최소 어항에 1마리 씩 더하기
    min_fishes = min(cage_map[-1])
    for k, v in enumerate(cage_map[-1]):
        if min_fishes == v:
            cage_map[-1][k] += 1
            
    # 가장 왼쪽을 쌓기
    cage_map.appendleft(cage_map[-1][:1:])
    cage_map[-1] = cage_map[-1][1::]
    
    # 될때까지 굴리기
    height = 0
    for level in cage_map:
        if level : 
            height += 1
    length = len(cage_map[-1])
    width = 1
    new_cage_map = []
    while height <= length - width:    
        for c in range(width):
            tmp = []
            for r in range(height):
                tmp.append(cage_map[r][c])
            new_cage_map.append(tmp[::-1])
        new_cage_map.append(cage_map[-1][width::])
        
        cage_map = new_cage_map[::]
        width = height
        height = 0
        for level in cage_map:
            if level : 
                height += 1
        length = len(cage_map[-1])
        new_cage_map = []
        
    # 조절하기
    operations = []
    for r in range(len(cage_map)):
        for c in range(len(cage_map[-1])):
            if len(cage_map[r]) <= c:
                continue
            # 오른쪽 비교
            if c + 1 < len(cage_map[r]):
                cur_val = cage_map[r][c]
                next_val = cage_map[r][c + 1]
                d = abs(next_val - cur_val) // 5
                if d > 0:
                    if cur_val > next_val:
                        operations.append((r, c, -d))
                        operations.append((r, c + 1, d))
                    elif cur_val < next_val:
                        operations.append((r, c, d))
                        operations.append((r, c + 1, -d))            
            # 하단 비교
            if r + 1 < len(cage_map):
                cur_val = cage_map[r][c]
                next_val = cage_map[r + 1][c]
                d = abs(next_val - cur_val) // 5
                if d > 0:
                    if cur_val > next_val:
                        operations.append((r, c, -d))
                        operations.append((r + 1, c, d))
                    elif cur_val < next_val:
                        operations.append((r, c, d))
                        operations.append((r + 1, c, -d))
    for r, c, d in operations:
        cage_map[r][c] += d     
        
    # 1단으로 재배열
    tmp = []
    for c in range(len(cage_map[-1])):   
        for r in range(len(cage_map)-1, -1, -1):
            if len(cage_map[r]) <= c:
                continue
            tmp.append(cage_map[r][c])
    cage_map = [tmp[::]]
    
    # 절반씩 두 번 굴리기 (N/2, N/4)
    # N/2
    tmp = []
    tmp.append(list(reversed(cage_map[-1][:len(cage_map[-1]) // 2:])))
    tmp.append(cage_map[-1][len(cage_map[-1]) // 2::])
    cage_map = tmp[::]
    
    # N/4
    new_cage_map = []
    width = len(cage_map[-1])
    height = len(cage_map)
    # LEFT HALF
    for r in range(height -1, -1, -1):
        tmp = []
        for c in range(width // 2 - 1, -1, -1):
            tmp.append(cage_map[r][c])
        new_cage_map.append(tmp)
    # RIGHT HALF
    for r in range(height):
        tmp = []
        for c in range(width // 2, width):
            tmp.append(cage_map[r][c])
        new_cage_map.append(tmp)
    cage_map = new_cage_map[::]
    
    # 조절하기
    operations = []
    for r in range(len(cage_map)):
        for c in range(len(cage_map[-1])):
            if len(cage_map[r]) <= c:
                continue
            # 오른쪽 비교
            if c + 1 < len(cage_map[r]):
                cur_val = cage_map[r][c]
                next_val = cage_map[r][c + 1]
                d = abs(next_val - cur_val) // 5
                if d > 0:
                    if cur_val > next_val:
                        operations.append((r, c, -d))
                        operations.append((r, c + 1, d))
                    elif cur_val < next_val:
                        operations.append((r, c, d))
                        operations.append((r, c + 1, -d))            
            # 하단 비교
            if r + 1 < len(cage_map):
                cur_val = cage_map[r][c]
                next_val = cage_map[r + 1][c]
                d = abs(next_val - cur_val) // 5
                if d > 0:
                    if cur_val > next_val:
                        operations.append((r, c, -d))
                        operations.append((r + 1, c, d))
                    elif cur_val < next_val:
                        operations.append((r, c, d))
                        operations.append((r + 1, c, -d))
    for r, c, d in operations:
        cage_map[r][c] += d     
        
    # 1단으로 재배열
    tmp = []
    for c in range(len(cage_map[-1])):   
        for r in range(len(cage_map)-1, -1, -1):
            if len(cage_map[r]) <= c:
                continue

            tmp.append(cage_map[r][c])
    cage_map = deque([tmp[::]])
                
def find_diff():
    max_val = max(max(i) for i in cage_map)
    min_val = min(min(i) for i in cage_map)
    return max_val - min_val
        
cnt = 0      
while MAX_DIFF < find_diff():
    organize()
    cnt += 1
print(cnt)