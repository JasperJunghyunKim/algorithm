# ########################################
# # Bottom Up
# import sys
# n = int(sys.stdin.readline().strip())
# price_list = [0] + list(map(int, sys.stdin.readline().strip().split()))
# max_price_list = [0, price_list[1], ]

# for i in range(2, n + 1):
#     max_price_list.append(max([price_list[i], *[max_price_list[j] + max_price_list[i-j] for j in range(1, i//2 + 1)]]))

# print(max_price_list[n])


########################################
# Top Down
import sys
sys.setrecursionlimit(10000)
n = int(sys.stdin.readline().strip())
price_list = [0] + list(map(int, sys.stdin.readline().strip().split()))
max_price_list = dict()

def find_max_price(n):
    if max_price_list.get(n) == None:
        max_price_list[n] = max([price_list[n], *[find_max_price(i) + find_max_price(n-i) for i in range(1, n//2 + 1)]])
    return max_price_list.get(n)

print(find_max_price(n))



# n = int(input())
# cmax_price = {0:0, 1: price_per_pack[0]}

# def find_max_price(n):
#     try:
#         return max_price[n]
#     except:
#         temp = [price_per_pack[n-1], ]
#         for i in range(1, n//2+1):
#             temp.append(find_max_price(i) + find_max_price(n-i))
#         max_price[n] = max(temp)
#         return max_price[n]

# print(find_max_price(n))


# # 2
# n = int(input())
# price_list = [0] + list(map(int, input().split()))

# for i in range(2, n+1):
#     price_list[i] = max((price_list[i-j] + price_list[j] for j in range(i//2 + 1)))

# print(price_list[n])
    
