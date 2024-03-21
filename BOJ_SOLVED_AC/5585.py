change = 1000 - int(input())
change_cnt = 0
coins = [500, 100, 50, 10, 5, 1]

for i in coins:
    change_cnt += change // i
    change -= i * (change // i)
print(change_cnt)

# while True:
#     if change == 0:
#         break
#     if change >= 500:
#         change -= 500
#         change_cnt += 1
#         continue
#     if change >= 100:
#         change -= 100
#         change_cnt += 1
#         continue
#     if change >= 50:
#         change -= 50
#         change_cnt += 1
#         continue
#     if change >= 10:
#         change -= 10
#         change_cnt += 1
#         continue
#     if change >= 5:
#         change -= 5
#         change_cnt += 1
#         continue
#     if change >= 1:
#         change -= 1
#         change_cnt += 1
#         continue
# print(change_cnt)