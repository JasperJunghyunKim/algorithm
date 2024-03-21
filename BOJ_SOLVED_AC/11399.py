import sys
sys_input = sys.stdin.readline

num_people = int(sys_input())
drawing_time = list(map(int, sys_input().split(' ')))
drawing_time.sort()
waiting_time = [0] * num_people
waiting_time[0] = drawing_time[0]
for i in range(1, num_people):
    waiting_time[i] = waiting_time[i-1] + drawing_time[i]
print(sum(waiting_time))