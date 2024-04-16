import sys
sys_input = sys.stdin.readline

n = int(sys_input().strip())
numbers = [0] * (n)

for i in range(n):
    numbers[i] = int(sys_input().strip())

print(*sorted(numbers), sep="\n")