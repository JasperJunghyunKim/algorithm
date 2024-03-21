# 
# 24-03-16
# 종료시간이 빠른 순, 시작시간이 늦은 순 -> 둘 다 정답
# 

# T2 시작시간이 늦은 순
import sys
sys_input = sys.stdin.readline

n = int(sys_input().strip())

meetings = [tuple(map(int, sys_input().split())) for _ in range(n)]

meetings.sort(key=lambda x: (x[0], x[1]), reverse=True)

cur_starttime = meetings[0][1]
num_meetings = 0

for starttime, endtime in meetings:
    if endtime <= cur_starttime:
        cur_starttime = starttime
        num_meetings += 1
        
print(num_meetings)

# T1 종료시간이 빠른 순
import sys
sys_input = sys.stdin.readline

n = int(sys_input().strip())

meetings = [tuple(map(int, sys_input().split())) for _ in range(n)]

meetings.sort(key=lambda x: (x[1], x[0]))

cur_endtime = 0
num_meetings = 0


for starttime, endtime in meetings:
    if starttime >= cur_endtime:
        num_meetings += 1
        cur_endtime = endtime

print(num_meetings)