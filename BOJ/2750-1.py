import sys
sys_input = sys.stdin.readline

n = int(sys_input())
numbers = []
for _ in range(n):
    numbers.append(int(sys_input().strip()))

print(*sorted(numbers), sep="\n")