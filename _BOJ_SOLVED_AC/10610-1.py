import sys
N = list(map(int, list(sys.stdin.readline().strip())))
total_sum = 0
for i in N:
    total_sum += i

# 3의 배수가 안된다면 불가
if total_sum % 3 != 0:
    print(-1)
    exit()

# 된다면
N.sort(reverse = True)
# print(N)
value = ''
for v in N:
    value += str(v)
value = int(value)

if value % 30 != 0:
    print(-1)
else:
    print(value)