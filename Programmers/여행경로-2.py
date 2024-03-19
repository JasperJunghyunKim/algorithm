#
# 24-03-18 T2
#
def solution(tickets):
    answer = []

    tickets.sort(key = lambda x : (x[0], x[1]))

    stack = []
    is_used = [False for _ in range(len(tickets))]
    cur_city = "ICN"
    answer.append(cur_city)
    for t_no, t in enumerate(tickets):
        if t[0] == "ICN": 
            stack.append(t)
            is_used[t_no] = True
            break
    
    while stack:
        cur_ticket = stack.pop()
        cur_city = cur_ticket[1]
        answer.append(cur_city)
        for t_no, t in enumerate(tickets):
            if t[0] == cur_city and not is_used[t_no]:
                stack.append(t)
                is_used[t_no] = True
                break            
    
    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	))
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	))



#
# 24-03-18 T1 : 시간초과
#
# def solution(tickets):
#     tickets.sort(key = lambda x : (x[0], x[1]))
#     cur_city = "ICN"
#     bounds = ["ICN", ]

#     while len(tickets):
#         for t_idx, ticket in enumerate(tickets):
#             if cur_city == ticket[0]:
#                 cur_city = ticket[1]
#                 bounds.append(ticket[1])    
#                 tickets = tickets[:t_idx] + tickets[t_idx + 1:]
#                 break

#     return bounds