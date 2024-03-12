#
# 24-03-12
#
import sys
sys_input = sys.stdin.readline
n = int(sys_input().strip())

red_cost = [0]
green_cost = [0]
blue_cost = [0]
red_min = [0] * (1 + n)
green_min = [0] * (1 + n)
blue_min = [0] * (1 + n)

for _ in range(n):
    r, g, b = map(int, sys_input().strip().split())
    red_cost.append(r)
    green_cost.append(g)
    blue_cost.append(b)
    
red_min[1] = red_cost[1]
green_min[1] = green_cost[1]
blue_min[1] = blue_cost[1]

for i in range(2, n + 1):
    red_min[i] = red_cost[i] + min(green_min[i-1], blue_min[i-1])
    green_min[i] = green_cost[i] + min(blue_min[i-1], red_min[i-1])
    blue_min[i] = blue_cost[i] + min(red_min[i-1], green_min[i-1])

print(min(red_min[n], green_min[n], blue_min[n]))