from collections import deque

def solution(n, computers):
    num_networks = 0
    
    to_visit = deque()
    visited = [False for _ in range(n)]
    
    for com_no, is_visited in enumerate(visited):
        if not is_visited:
            num_networks += 1
            to_visit.append(com_no)
            visited[com_no] = True
            
            while to_visit:
                cur_com = to_visit.popleft()
                for next_com, is_connected in enumerate(computers[cur_com]):
                    if cur_com == next_com: continue
                    if is_connected and visited[next_com] == False:
                        to_visit.append(next_com)
                        visited[next_com] = True
    
    return num_networks