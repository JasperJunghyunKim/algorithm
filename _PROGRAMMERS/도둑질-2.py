def solution(money):
    num_houses = len(money)
    dp_1_selected = [0 for i in range(num_houses)]
    dp_1_not_selected = [0 for i in range(num_houses)]

    # first select
    dp_1_selected[0] = money[0]
    dp_1_selected[1] = money[0]
    for i in range(2, num_houses - 1):
        dp_1_selected[i] = max(dp_1_selected[i-1], dp_1_selected[i-2] + money[i])

    # first not select
    dp_1_not_selected[0] = 0
    dp_1_not_selected[1] = money[1]
    for i in range(2, num_houses):
        dp_1_not_selected[i] = max(dp_1_not_selected[i - 1], dp_1_not_selected[i - 2] + money[i])

    return max(dp_1_selected[num_houses - 2], dp_1_not_selected[num_houses - 1])

money = [1,2,3,1]
print(solution(money))