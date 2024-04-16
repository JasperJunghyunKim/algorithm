import sys
sys_input = sys.stdin.readline

NUM_TC = int(sys_input())

for _ in range(NUM_TC):
    NUM_COINS = int(sys_input())
    coins = list(map(int, sys_input().split(' ')))
    TARGET = int(sys_input())
    
    