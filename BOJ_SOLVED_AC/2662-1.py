import sys
sys_input = sys.stdin.readline

INVEST, NUM_COMPANY = map(int, sys_input().strip().split())
profit = []
for _ in range(INVEST):
    profit.append(tuple(map(int, sys_input().strip().split())))

dp = [0] * (INVEST + 1)
for i in range(NUM_COMPANY):
    for invest in range(1, INVEST + 1):
        if 