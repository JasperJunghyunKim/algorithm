def is_valid_position(row):
    for i in range(row):
        # 같은 열 또는 대각선 상에 다른 퀸이 있는지 확인
        if board[row] == board[i] or abs(board[row] - board[i]) == row - i:
            return False
    return True

def dfs(row):
    global count
    if row == N:  # 모든 행에 퀸을 놓았다면, 하나의 해를 찾음
        count += 1
        return
    for col in range(N):
        board[row] = col  # 현재 행에 퀸을 놓음
        if is_valid_position(row):  # 유효한 위치인지 확인
            dfs(row + 1)  # 다음 행으로 이동

N = int(input())
board = [0] * N  # 각 행의 퀸이 놓인 열의 위치
count = 0
dfs(0)  # 0번째 행부터 시작
print(count)