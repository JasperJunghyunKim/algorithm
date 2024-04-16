from collections import deque

game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]

def solution(game_board, table):
    size = len(game_board)
    answer = -1

    def bfs(init_row, init_col):
        to_visit = deque()
        visited = []
        to_visit.append((init_row, init_col))
        visited.append((0, 0))
        while to_visit:
            cur_row, cur_col = to_visit.popleft()
            for dr, dc in [(0,1), (0,-1), (1,0), (-1, 0)]:
                next_row, next_col = cur_row + dr, cur_col + dc
                # in range
                # valid pixel
                # not visited
                if 0 <= next_row < size and 0 <= next_col < size:
                    if game_board[next_row][next_col] == 0:
                        if (init_row - next_row, init_col - next_col) not in visited:
                            to_visit.append((next_row, next_col))
                            visited.append((init_row - next_row, init_col - next_col))
        return visited

    for i in range(size):
        for j in range(size):
            if game_board[i][j] == 0:
                # do bfs
                
                
    return answer

print(solution(game_board, table))