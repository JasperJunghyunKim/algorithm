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

print(len(natural))