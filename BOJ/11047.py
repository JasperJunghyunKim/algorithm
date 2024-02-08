import sys
sys_input = sys.stdin.readline

num_coin, value = map(int, sys_input().split(' '))
coins = [int(sys_input()) for _ in range(num_coin)]

cnt = 0
for coin in coins[::-1]:
    cnt += value//coin
    value %= coin
print(cnt)