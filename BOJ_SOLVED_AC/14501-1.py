#
# 매일 두 가지의 상담이 있을 경우의 문제로 변형해서 풀어보자
#

import sys
import itertools
N = int(sys.stdin.readline().strip())
time = [0 for _ in range(N+1)]
price = [0 for _ in range(N+1)]
for i in range(1, N + 1):
    time[i], price[i] = map(int, sys.stdin.readline().strip().split())

max_value = 0

all_cases = []
for i in range(1 ,N + 1):
    all_cases.extend(list(itertools.combinations(range(1, N + 1), i)))

for c in all_cases:
    current_day = c[0]
    current_value = 0
    for day in c:
        if day < current_day: continue
        if day + time[day] - 1 <= N:
            current_day = day + time[day]
            current_value += price[day]
    max_value = current_value if current_value > max_value else max_value

print(max_value)
            
    