# 숫자 N 을 -> N = 1 + 2 + 3 + ... + a 이 될 때까지

n = int(input().strip())

natural = [n,]

temp = 1
while True:
    if natural[len(natural)-1] - temp <= temp:
        break
    else:
        end = natural.pop()
        natural.append(temp)
        natural.append(end - temp)
        temp += 1
    # print(natural)

print(len(natural))