########################################
# 23-12-15 (2)
# 시작시간이 가장 늦은 것 기준으로
# 이건 정답임 ... (왜지?)
import sys
START = 0
END = 1
sys_input = sys.stdin.readline
num_meetings = int(sys_input())
meetings = []
for _ in range(num_meetings):
    start, end = map(int, sys_input().split(' '))
    meetings.append([start, end])
meetings.sort(reverse=True)
cur_start = 2_147_483_647
cnt = 0
for meeting in meetings:
    if meeting[END] <= cur_start:
        cnt += 1
        cur_start = meeting[START]
print(cnt)
########################################
# 23-12-15 (1)
# 종료시간이 가장 빠른 것 기준으로 
# 채점 98% 쯤 가다가 틀림... sorting key 의 문제로 보임
# 
import sys
START = 1
END = 0
sys_input = sys.stdin.readline
num_meetings = int(sys_input())
meetings = []
for _ in range(num_meetings):
    start, end = map(int, sys_input().split(' '))
    meetings.append([end, start])

next_start = 0
meetings.sort(key = lambda meeting : meeting[END])
# meetings.sort(key = lambda meeting : (meeting[END], -meeting[START]))
# meetings.sort()
cnt = 0
for meeting in meetings:
    if next_start <= meeting[START]:
        cnt += 1
        next_start = meeting[END]
print(cnt)


# ########################################
# # 23-11-30
# import sys
# sys_input = sys.stdin.readline
# meetings = []
# num_meetings = int(sys_input())
# for i in range(num_meetings):
#     start, end = map(int, sys_input().split(' '))
#     meetings.append((end, start))
# meetings.sort()

# next_starttime = 0
# cnt = 0
# for endtime, starttime in meetings:
#     if next_starttime <= starttime:
#         cnt += 1
#         next_starttime = endtime
# print(cnt)