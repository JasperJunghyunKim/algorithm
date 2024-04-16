import heapq
n = 6
times = [7,10]

def solution(n, times):
    immigration = [(0, t) for t in times]
    max_time_cost = max(times)
    
    while n > 0:
        t_now, t_add = heapq.heappop(immigration)
        num_people = 1
        while t_now + t_add * num_people <= max_time_cost:
            num_people += 1
        num_people -= 1
        if num_people == 0:
            num_people = 1
        if num_people <= n:        
            n -= num_people
        elif num_people > n:
            num_people = n
            n = 0
        heapq.heappush(immigration, (t_now + t_add * num_people, t_add))
        max_time_cost = t_now + t_add * num_people if t_now + t_add * num_people > max_time_cost else max_time_cost
    
    return max_time_cost

print(solution(n, times))