import sys
sys_input = sys.stdin.readline

WEIGHT = 0
VALUE = 1

num_gems, num_bags = map(int, sys_input().split(' '))
gems = [] # weight, value
bags = [] # max_weight
for _ in range(num_gems):
    weight, value = map(int, sys_input().split(' '))
    gems.append((value, weight))
for _ in range(num_bags):
    bags.append(int(sys_input()))

gems.sort()
gems = gems[::-1]
bags.sort()
check_gems = [False for _ in range(num_gems)]
check_bags = [False for _ in range(num_bags)]

total_value = 0
for _ in range(num_bags):
    break_loop = False
    for i, gem in enumerate(gems):
        if check_gems[i] == True:
            continue
        for j, bag in enumerate(bags):
            if check_bags[j] == True:
                continue
            if gem[WEIGHT] <= bag:
                check_gems[i] = True
                check_bags[j] = True
                total_value += gem[VALUE]
                break_loop = True
                break
        if break_loop:
            break
print(total_value)