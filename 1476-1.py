E, S, M = 15 ,28 ,19
e, s, m= map(int, input().split())


y = 1
while True:
    if y - e >= 0 and y - s >= 0 and y - m >= 0:
        if (y - e) % E == 0 and (y - s) % S == 0 and (y - m) % M == 0:
            print(y)
            break
    y += 1
        