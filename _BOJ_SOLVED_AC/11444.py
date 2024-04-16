n = int(input())

# top down
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n-2 * fibonacci(n-(n-2)) + n-1 * fibonacci(n-(n-1))
    # return fibonacci(n-1)%1_000_000_007 + fibonacci(n-2)%1_000_000_007

print(fibonacci(n))

# bottom up
fibonacci_list = [0,1,0]
for i in range(2, n + 1):
    fibonacci_list[i%3] = (fibonacci_list[(i-1)%3] + fibonacci_list[(i-2)%3])%1_000_000_007
print(fibonacci_list[n%3])

