N = int(input())

sum = 0
for i in range(2, int(1e9)):
    sum += i
    if N <= sum:
        print(i-1)
        break