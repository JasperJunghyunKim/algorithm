import sys
input = sys.stdin.readline
origami = []

n = int(input())
for _ in range(n):
    origami.append(list(map(int, input().split(' '))))

num_white = 0
num_blue = 0

def cut_origami(origmai_size, row_start, col_start):
    global num_white
    global num_blue
    
    first_piece = origami[row_start][col_start]

    for i in range(row_start, row_start + origmai_size):
        for j in range(col_start, col_start + origmai_size):
            # 색깔이 다를 경우
            if first_piece != origami[i][j]:
                # upper left
                cut_origami(origmai_size//2, row_start, col_start)
                # upper right
                cut_origami(origmai_size//2, row_start, col_start + origmai_size//2)
                # lower left
                cut_origami(origmai_size//2, row_start + origmai_size//2, col_start)
                # lower right
                cut_origami(origmai_size//2, row_start + origmai_size//2, col_start + origmai_size//2)
                return
    else:
        if first_piece == 0:
            num_white += 1
        elif first_piece == 1:
            num_blue += 1
        return
        
# 오류 코드
# 파라미터를 start, end 식으로 줘버리면 다음 재귀 함수에 end//2 로 넣었을 때 범위가 오류가 난다.
# 예를 들어 N = 32 에서 divide(16, 24, 16, 24) 를 하게되면 upper_left 부터 (16, 12, 16, 12) 가 나오는 오류가 생김
# 이부분 오류 찾는데 시간 오래 걸렸음 (23-11-25) 
def divide(row_start, row_end, col_start, col_end):
    global num_white
    global num_blue
    
    first_color = origami[row_start][col_start]

    for i in range(row_start, row_end):
        for j in range(col_start, col_end):
            if first_color != origami[i][j]:
                # upper left
                divide(row_start, row_end//2, col_start, col_end//2)
                # upper right
                divide(row_start, row_end//2, col_end//2, col_end)
                # lower left
                divide(row_end//2, row_end, col_start, col_end//2)
                # lower right
                divide(row_end//2, row_end, col_end//2, col_end)
                return
    else:
        if first_color == 0:
            num_white += 1
        elif first_color == 1:
            num_blue += 1
        return
        
# divide(0, len(origami), 0, len(origami))
cut_origami(len(origami), 0, 0)
print(num_white)
print(num_blue)