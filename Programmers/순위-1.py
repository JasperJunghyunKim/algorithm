#
# 24-03-20
# GPT 힌트 얻음
# 플로이드워셜을 사용할 수도 있으나, 개념이 불확실한 관계로 BFS를 사용
#
# win, lose 라는 방향성 그래프를 생성하고 각 선수마다 BFS 를 실행했을 때, 
# 해당 선수보다 순위가 낮은 선수 수, 높은 선수 수를 구할 수 있음
#
from collections import deque

def solution(n, results):
    
    answer = 0
    wins = {i:[] for i in range(1, n + 1)}
    loses = {i:[] for i in range(1, n + 1)}
    for winner, loser in results:
        wins[winner].append(loser)
        loses[loser].append(winner)
    
    
    # find each players, find num_players of lower rank, higher rank
    for player in range(1, n + 1):
        # get num of lower ranks
        visited = [False] * (n + 1)
        to_visit = deque()
        visited[player] = True
        to_visit.append(player)
        
        num_players_lower = 0
        while to_visit:
            cur_player = to_visit.popleft()
            for next_player in wins[cur_player]:
                if visited[next_player] == False:
                    num_players_lower += 1
                    visited[next_player] = True
                    to_visit.append(next_player)
        
        # get num of higher ranks
        visited = [False] * (n + 1)
        to_visit = deque()
        visited[player] = True
        to_visit.append(player)
        
        num_players_higer = 0
        while to_visit:
            cur_player = to_visit.popleft()
            for next_player in loses[cur_player]:
                if visited[next_player] == False:
                    num_players_higer += 1
                    visited[next_player] = True
                    to_visit.append(next_player)
                       
        if num_players_higer + num_players_lower == n - 1:
            answer += 1
    
    return answer

if __name__ == "__main__":
    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	
    print(solution(n, results))