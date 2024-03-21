import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split(' '))) for _ in range(n)]
cnt = [0,0,0] # 0, 1, -1

def divide(size_paper, row_start, col_start):

    first_pixel = paper[row_start][col_start]
    
    for i in range(row_start, row_start + size_paper):
        for j in range(col_start, col_start + size_paper):
            if first_pixel != paper[i][j]:
                size_third = size_paper//3
                # top
                divide(size_third, row_start, col_start)
                divide(size_third, row_start, col_start + size_third)
                divide(size_third, row_start, col_start + (size_third)*2)
                # mid
                divide(size_third, row_start + size_third, col_start)
                divide(size_third, row_start + size_third, col_start + size_third)
                divide(size_third, row_start + size_third, col_start + (size_third)*2)
                # bottom
                divide(size_third, row_start + (size_third)*2, col_start)
                divide(size_third, row_start + (size_third)*2, col_start + size_third)
                divide(size_third, row_start + (size_third)*2, col_start + (size_third)*2)
                return
    else:
        cnt[first_pixel] += 1
        return
    
divide(len(paper), 0, 0)
print(cnt[-1], cnt[0], cnt[1], sep='\n')