N = int(input())

def hanoi(move_from, move_to, height):
    if height == 1:
        print(move_from, move_to)
        return

    detour = None
    if move_from * move_to == 2: detour = 3
    elif move_from * move_to == 3: detour = 2
    elif move_from * move_to == 6: detour = 1

    hanoi(move_from, detour, height - 1)
    hanoi(move_from, move_to, 1)
    hanoi(detour, move_to, height - 1)

dp = [0] * (N + 1)
dp[1] = 1
for i in range(2, N + 1):
    dp[i] = 2 * dp[i-1] + 1

if N <= 20:
    print(dp[N])
    hanoi(1, 3, N)
else:
    print(dp[N])