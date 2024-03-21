N = int(input())
for i in range(1, 2 * N):
    i = abs(N - i)
    for _ in range(i):
        print(" ", end = "")
    for _ in range((2 * N) - 1 - (2 * i)):
        print("*", end = "")
    # for _ in range(i):
    #     print(" ", end = "")
    print("")