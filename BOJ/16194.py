import sys
n = int(sys.stdin.readline().strip())
price_list = [0] + list(map(int, sys.stdin.readline().strip().split()))
min_price_list = [0, price_list[1]]

for i in range(2, n + 1):
    min_price_list.append(min([price_list[i], *[min_price_list[j] + min_price_list[i-j] for j in range(1, i//2+1)]]))

print(min_price_list[n])