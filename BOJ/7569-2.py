import sys
sys_input = sys.stdin.readline

col, row, height = map(int, sys_input().split())

tomato_box = [[] for _ in range(height)]

for h in range(height):
    for _ in range(row):
        tomato_box[h].append(list(map(int, sys_input().split())))

tomato[]