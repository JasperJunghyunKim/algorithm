a, b, c = map(int, input().split(' '))
memo = dict()
def divide(a, b):
    if memo.get(b) != None:
        return memo.get(b)
    else:
        if b <= 1:
            return a ** b
        else:
            memo.update({b//2: divide(a, b//2)%c})
            memo.update({b-b//2: divide(a, b - b//2)%c})
            return (divide(a, b//2) * divide(a, b - b//2))%c

print(divide(a, b)%c)