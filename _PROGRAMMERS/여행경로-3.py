#
# 24-03-19
# DFS, 백트래킹
#

# T3 - GPT
# Stack, 인접리스트
def solution(tickets):
    graph = {}
    for dept, arrv in sorted(tickets, reverse=True):
        if dept in graph:
            graph[dept].append(arrv)
        else:
            graph[dept] = [arrv]
    
    stack = ["ICN"]
    path = []
    
    while stack:
        cur_city = stack[-1]
        # cur_city 에서 출발할 수 있으면, 도착지를 스택에 넣음
        if cur_city in graph and graph[cur_city]:
            stack.append(graph[cur_city].pop())
        # 
        else:
            path.append(stack.pop())

# T2 - GPT
# Recursive, 인접리스트
def solution(tickets):
    
    graph = {}
    for start, end in tickets:
        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = [end]
    
    for start in graph.keys():
        graph[start].sort(reversed = True)
    
    path = []
    
    def dfs(airport):
        while airport in graph and graph[airport] :
            next_airport = graph[airport].pop()
            dfs(next_airport)
        path.append(airport)

    dfs("ICN")
    return path[::-1]





# T1 
DEPT = 0
ARRV = 1

def solution(tickets):
    
    tickets.sort(key = lambda x : (x[0], x[1]))
    tickets_used = []
    bounds = ['ICN']
    cur_city = "ICN"
    
    def use_ticket(t_no):
        tickets_used.append(t_no)
        
        # 모든 티켓을 사용하게 되면, bound 리스트를 생성하고 리턴
        if len(tickets_used) == len(tickets):
            for t_no in tickets_used:
                bounds.append(tickets[t_no][ARRV])
            return

        # 다음 목적지를 변경하고, 사용할 티켓을 찾음
        cur_city = tickets[tickets_used[-1]][ARRV]
        for t_no, ticket in enumerate(tickets):
            if ticket[DEPT] == cur_city and t_no not in tickets_used:
                use_ticket(t_no)
        
        # for 모두 순회했을 때, A. 재귀 탈출조건 B. 백트래킹 조건
        else:
            if len(tickets_used) == len(tickets):
                return
            else:
                tickets_used.pop()   
    
    for t_no, ticket in enumerate(tickets):
        if ticket[DEPT] == cur_city and t_no not in tickets_used:
            use_ticket(t_no)
            
    return bounds

# tickets = [["ICN", "JFK"], ["JFK", "ICN"], ["ICN", "JFK"], ["JFK", "ICN"], ["ICN", "JFK"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "AAA"], ["ICN", "BBB"], ["BBB", "ICN"]]

print(solution(tickets))