########################################
# 23-12-14
import sys
sys_input = sys.stdin.readline

num_houses = int(sys_input())
red = []
green = []
blue = []
for _ in range(num_houses):
    r, g, b = map(int, sys_input().split(' '))
    red.append(r)
    green.append(g)
    blue.append(b)

for i in range(1, num_houses):
    red[i] = red[i] + min(green[i-1], blue[i-1])
    green[i] = green[i] + min(blue[i-1], red[i-1])
    blue[i] = blue[i] + min(red[i-1], green[i-1])

print(min(red[num_houses-1], green[num_houses-1], blue[num_houses-1]))


########################################
# 23-11-07
# 풀이 참조함
import sys
input = sys.stdin.readline
n = int(input())
cost = []
for i in range(n):
    cost.append(list(map(int, input().split())))

for i in range(1, n):
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0]
    cost[i][1] = min(cost[i-1][2], cost[i-1][0]) + cost[i][1]
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + cost[i][2]

print(min(cost[n-1][0], cost[n-1][1], cost[n-1][2]))