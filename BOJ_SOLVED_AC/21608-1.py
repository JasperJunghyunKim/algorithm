import sys
sys_input = sys.stdin.readline

N = int(sys_input().strip())
classroom = [[0 for _ in range(N)] for _ in range(N)]
empty = {(r, c): True for c in range(N) for r in range(N)}
crush = [list() for _ in range(N * N + 1)]
total_satisfaction = 0

def set_student(me, c1, c2, c3, c4):
    
    def remove_canidate(candidate, max_value):
        candidate = {k:v for k,v in candidate.items() if v == max_value}
        return candidate
    
    # 후보군 생성
    crush = [c1, c2, c3, c4]
    candidate = {(r,c):0 for c in range(N) for r in range(N) if classroom[r][c] == 0}
    
    # 조건 1
    # 각 후보군마다, 좋아하는 학생 수만큼 계산
    for cur_r, cur_c in candidate.keys():
        for d_r, d_c in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_r, next_c = cur_r + d_r, cur_c + d_c
            if 0 <= next_r < N and 0 <= next_c < N:
                if classroom[next_r][next_c] in crush:
                    candidate[(cur_r, cur_c)] += 1
    
    # 후보군 중에 최대가 아닌 나머지를 제거
    candidate = remove_canidate(candidate, max(candidate.values()))         
    
    # 후보가 하나라면 학생을 배치하고 리턴
    if len(candidate) == 1: 
        for r, c in candidate.keys():
            classroom[r][c] = me
        return
            
    # 조건 2
    # 각 후보군마다, 인접한 빈 공간의 개수를 계산
    candidate = {k:0 for k in candidate.keys()}      
    for cur_r, cur_c in candidate.keys():
        for d_r, d_c in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_r, next_c = cur_r + d_r, cur_c + d_c
            if 0 <= next_r < N and 0 <= next_c < N:
                if classroom[next_r][next_c] == 0:
                    candidate[(cur_r, cur_c)] += 1
                    
    # 후보군 중에 최대가 아닌 나머지를 제거
    candidate = remove_canidate(candidate, max(candidate.values()))         
    
    # 후보가 하나라면 학생을 배치하고 리턴
    if len(candidate) == 1: 
        for r, c in candidate.keys():
            classroom[r][c] = me
        return
                    
    # 조건 3
    min_r, min_c = min(candidate.keys())
    classroom[min_r][min_c] = me
    return
    

for i in range(N * N):
    me, c1, c2, c3, c4 = map(int, sys_input().strip().split())
    set_student(me, c1, c2, c3, c4)
    crush[me] = [c1, c2, c3, c4]
    
for cur_r in range(N):
    for cur_c in range(N):
        my_satisfaction = 0
        me = classroom[cur_r][cur_c]
        for d_r, d_c in [(0,1), (0,-1), (1,0), (-1,0)]:
            next_r, next_c = cur_r + d_r, cur_c + d_c
            if 0 <= next_r < N and 0 <= next_c < N:
                if classroom[next_r][next_c] in crush[me]:
                    my_satisfaction += 1
        
        if my_satisfaction == 1:
            total_satisfaction += 1
        elif my_satisfaction == 2:
            total_satisfaction += 10
        elif my_satisfaction == 3:
            total_satisfaction += 100
        elif my_satisfaction == 4:
            total_satisfaction += 1000

print(total_satisfaction)