n, k = map(int, input().split())

memo = dict({1:1})
def factorial(n):
    if memo.get(n) != None:
        return memo.get(n)
    else:
        memo.update({n:n*factorial(n-1)%1_000_000_007})
        return memo.get(n)

print((factorial(n)/(factorial(n-k)*factorial(k)))%1_000_000_007)