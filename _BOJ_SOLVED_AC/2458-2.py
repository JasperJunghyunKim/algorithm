import sys
sys_input = sys.stdin.readline

NUM_STUDENT, NUM_COMPARE = map(int, sys_input().strip().split())

fw = [[False for _ in range(NUM_STUDENT + 1)] for _ in range(NUM_STUDENT + 1)]



for i in range(NUM_STUDENT + 1):
    fw[i][i] = True
for _ in range(NUM_COMPARE):
    smaller, taller = map(int, sys_input().strip().split())
    fw[smaller][taller] = True

# floyd-warshall
# T1 : 루프 순서가 잘못 되었으므로, 제대로 갱신되지 않음
# for a in range(1, NUM_STUDENT + 1):
#     for b in range(1, NUM_STUDENT + 1):
#         if fw[a][b] == True: continue
#         for stopover in range(1, NUM_STUDENT + 1):
#             if fw[a][stopover] and fw[stopover][b]:                
#                 fw[a][b] = True
#                 break
# T2 : 정답 
for stopover in range(NUM_STUDENT + 1):
    for a in range(NUM_STUDENT + 1):
        for b in range(NUM_STUDENT + 1):
            if fw[a][stopover] and fw[stopover][b]:
                fw[a][b] = True

cnt = 0
for student in range(1, NUM_STUDENT + 1):
    num_know = 0
    for next_student in range(1, NUM_STUDENT + 1):
        if student == next_student: 
            continue
        if fw[student][next_student] or fw[next_student][student]: 
            num_know += 1
    if NUM_STUDENT - 1 == num_know: 
        cnt += 1

print(cnt)