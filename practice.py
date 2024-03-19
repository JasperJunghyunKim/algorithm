def solution(tickets):
    tickets.sort(key = lambda x : (x[0], x[1]))
    cur_city = "ICN"
    bounds = ["ICN", ]

    while len(tickets):
        for t_idx, ticket in enumerate(tickets):
            if cur_city == ticket[0]:
                cur_city = ticket[1]
                bounds.append(ticket[1])    
                tickets = tickets[:t_idx] + tickets[t_idx + 1:]
                break


    return bounds

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))