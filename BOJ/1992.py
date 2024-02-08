import sys
input = sys.stdin.readline

n = int(input())
video = [list(input().strip()) for _ in range(n)]
quad_tree = []


def compress(size_video, row_start, col_start):
    first_pixel = video[row_start][col_start]

    for i in range(row_start, row_start + size_video):
        for j in range(col_start, col_start + size_video):
            if first_pixel != video[i][j]:
                quad_tree.append('(')
                compress(size_video//2, row_start, col_start)
                compress(size_video//2, row_start, col_start + size_video//2)
                compress(size_video//2, row_start + size_video//2, col_start)
                compress(size_video//2, row_start + size_video//2, col_start + size_video//2)
                quad_tree.append(')')
                return
    else:
        if first_pixel == '1':
            quad_tree.append(1)
        elif first_pixel == '0':
            quad_tree.append(0)
        return
    
compress(len(video), 0, 0)
for i in quad_tree:
    print(i, end='')
