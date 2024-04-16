import sys
sys_input = sys.stdin.readline

num_students = int(sys_input())
wish = [int(sys_input()) for _ in range(num_students)]
wish.sort()

complaint = 0
for i in range(1, num_students + 1):
    complaint += abs(wish[i-1] - i)
print(complaint)