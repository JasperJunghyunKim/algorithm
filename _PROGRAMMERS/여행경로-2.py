#
# 24-03-18 T1 : 시간초과
# 아래 코드의 경우 다음 케이스를 통과하지 못함 : [["ICN", "AAA"], ["ICN", "BBB"], ["BBB", "AAA"]]
# 'AAA' 로 가는 것 부터 선택하는데, 'AAA' 에서 출발하는 티켓이 없기 때문에 무한루프에 빠지면서 시간초과
# 따라서 DFS를 활용한 백트래킹 전략으로 해결해야 됨
#
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