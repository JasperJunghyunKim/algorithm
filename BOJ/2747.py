########################################
# 23-12-14
import sys
sys_input = sys.stdin.readline
n = int(sys_input().strip())

arr = [0 for _ in range(46)]
arr[0] = 0
arr[1] = 1
for i in range(2,n+1):
    arr[i] = arr[i-1] + arr[i-2]
print(arr[n])

########################################
# 23-11-07 (2)
import sys
n = int(sys.stdin.readline().strip())

fibo_list = [0, 1]
for i in range(2, n + 1):
    fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
print(fibo_list[n])

########################################
# 23-11-07 (1)
# 시간초과
n = int(input().strip())

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(n))

