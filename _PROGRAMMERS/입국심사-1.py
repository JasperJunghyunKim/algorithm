def solution(n, times):
    MAX_TIME = n * max(times)

    # binary search
    low = 1
    high = MAX_TIME
    while low <= high:
        # check_time == mid
        check_time = (low + high) // 2
        num_passed = 0
        for t in times:
            num_passed += check_time // t
        if num_passed >= n:
            high = check_time - 1
        elif num_passed < n:
            low = check_time + 1


    return low

n = 6
times = [7, 10]
print(solution(n, times))