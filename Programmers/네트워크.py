from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            answer += 1
            to_visit = deque()
            to_visit.append(i)
            visited[i] = True
            while to_visit:
                cur_computer = to_visit.popleft()
                for next_computer, connected in enumerate(computers[cur_computer]):
                    if connected == 1:
                        if visited[next_computer] == False:
                            to_visit.append(next_computer)
                            visited[next_computer] = True
    
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]	))