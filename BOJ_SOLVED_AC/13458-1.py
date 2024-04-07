import sys
import math
sys_input = sys.stdin.readline

NUM_ROOM = int(sys_input().strip())
rooms = list(map(int, sys_input().strip().split()))
MAIN, SUB = map(int, sys_input().strip().split())

# 주 감독관은 고사장 수 만큼 존재
total_supervisors = NUM_ROOM

# 
for room in rooms:
    rest = room - MAIN
    if rest <= 0:
        continue
    total_supervisors += math.ceil((rest) / SUB)

print(total_supervisors)
        