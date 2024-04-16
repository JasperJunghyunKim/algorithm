from collections import deque
MAX_RADIUS, NUM_NUMBERS, NUM_CMD = map(int, input().strip().split())
CLOCK = 0
COUNTER = 1
total_num_numbers = 0
total_sum = 0
board = [[]]
for _ in range(MAX_RADIUS):
    board.append(list(map(int, input().strip().split())))
    
for r in range(1, MAX_RADIUS + 1):
    for c in range(NUM_NUMBERS):
        if board[r][c]: 
            total_num_numbers += 1
            total_sum += board[r][c]

def rotate(multiple_r, d, k):
    k = k % NUM_NUMBERS
    # 이동 횟수가 같을 경우, 변함이 없음
    if k == NUM_NUMBERS or k == 0:
        return
    for r in range(1, MAX_RADIUS + 1):
        if r % multiple_r == 0:
            # 뒤가 앞으로
            if d == CLOCK:
                front = board[r][:NUM_NUMBERS - k]
                back = board[r][NUM_NUMBERS - k:]
                board[r] = back + front
            # 앞이 뒤로
            elif d == COUNTER:
                front = board[r][:k]
                back = board[r][k:]
                board[r] = back + front

def for_adjacent():
    global total_num_numbers
    global total_sum
    is_adjacent = False
    for cur_r in range(1, MAX_RADIUS + 1):
        # 원판에 수가 전부 지워졌으면 패스
        if sum(board[cur_r]) == 0: continue
        #
        else: 
            for cur_c in range(NUM_NUMBERS):
                if board[cur_r][cur_c] != 0:
                    # cur_r, cur_c 에 대하여 BFS 
                    tmp_ajdacent = False
                    cur_val = board[cur_r][cur_c]
                    visited = {(cur_r, cur_c): True}
                    to_visit = deque([(cur_r, cur_c)])
                    while to_visit:
                        ccr, ccc = to_visit.popleft()
                        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                            next_r, next_c = ccr + dr, ccc + dc
                            if not (1 <= next_r <= MAX_RADIUS): continue
                            next_c = (next_c + NUM_NUMBERS) % NUM_NUMBERS
                            if board[next_r][next_c] == cur_val and (next_r, next_c) not in visited:
                                tmp_ajdacent = True
                                visited[(next_r, next_c)] = True
                                to_visit.append((next_r, next_c))
                    if tmp_ajdacent:
                        is_adjacent = True
                        for r, c in visited.keys():
                            board[r][c] = 0
                            total_num_numbers -= 1
                            total_sum -= cur_val
                
                        
    if not is_adjacent:
        if total_num_numbers == 0:
            return
        average = (total_sum / total_num_numbers)
        for r in range(1, MAX_RADIUS + 1):
            for c in range(NUM_NUMBERS):
                if board[r][c] > average:
                    board[r][c] -= 1
                    total_sum -= 1
                    if board[r][c] == 0:
                        total_num_numbers -= 1
                elif board[r][c] < average and board[r][c] != 0:
                    board[r][c] += 1
                    total_sum += 1
        
                    
            

for _ in range(NUM_CMD):
    multiple_r, d, k = map(int, input().strip().split())
    rotate(multiple_r, d, k)
    # print(*board, sep="\n")

    for_adjacent()
    # print(*board, sep="\n")

print(total_sum)


