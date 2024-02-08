from collections import deque

# tickets = [["ICN", "JFK"], ["JFK", "ICN"], ["ICN", "JFK"], ["JFK", "ICN"], ["ICN", "JFK"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]

def solution(tickets):
    num_tickets = len(tickets)
    temp = []

    to_visit = deque()
    for index, (departure, arrival) in enumerate(tickets):
        if departure == 'ICN':
            to_visit.append((arrival, [index]))
    while to_visit:
        cur_city, used_tickets = to_visit.pop()
        if len(used_tickets) == num_tickets:
            temp.append(used_tickets)
        for index, (departure, arrival) in enumerate(tickets):
            if cur_city == departure and index not in used_tickets:
                tmp = used_tickets[::]
                tmp.append(index)
                to_visit.append((arrival, tmp))

    # temp 를 실제 경로명으로 치환
    for i in temp:
        for k, j in enumerate(i):
            i[k] = tickets[j]
    temp = min(temp)
    answer = []
    answer.append(temp[0][0])
    for i in temp: answer.append(i[1])
    return answer

print(solution(tickets))