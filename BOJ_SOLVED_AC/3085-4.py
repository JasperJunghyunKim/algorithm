#
# 24-03-21
# map[i][j]에서 우, 하를 swap하는 것은, map[i+1][j+1] 좌, 상을 swap 하는 것과 같음 -> 중복 제거하는 것이 핵심
# find_longest 를 구할 때도, map 전체를 탐색하지 않고, 변경된 좌표 기준으로 row, col 만 탐색
#
import sys

def solution():
    sys_input = sys.stdin.readline
    N = int(sys_input().strip())
    candy_map = [None] * N
    longest_candies = 0
    for i in range(N):
        candy_map[i] = list(sys_input().strip())

    def find_longest(r1, r2, c1, c2):
        the_longest = 0
        
        # row 에서 찾기
        for row in range(N):
            row_longest = 1
            for col in range(1, N):
                if candy_map[row][col] == candy_map[row][col - 1]:
                    row_longest += 1
                    the_longest = row_longest if row_longest > the_longest else the_longest
                else:
                    row_longest = 1
        
        # col
        for col in range(N):
            col_longest = 1
            for row in range(1, N):
                if candy_map[row][col] == candy_map[row - 1][col]:
                    col_longest += 1
                    the_longest = col_longest if col_longest > the_longest else the_longest
                else:
                    col_longest = 1
        
        return the_longest

    for c_r in range(N):
        for c_c in range(N):
            if c_r + 1 < N and candy_map[c_r][c_c] != candy_map[c_r + 1][c_c]:
                candy_map[c_r][c_c], candy_map[c_r + 1][c_c] = candy_map[c_r + 1][c_c], candy_map[c_r][c_c]
                d = find_longest(c_r, c_r + 1, c_c, c_c)
                longest_candies = d if d > longest_candies else longest_candies
                candy_map[c_r][c_c], candy_map[c_r + 1][c_c] = candy_map[c_r + 1][c_c], candy_map[c_r][c_c]
            if c_c + 1 < N and candy_map[c_r][c_c] != candy_map[c_r][c_c + 1]:
                candy_map[c_r][c_c], candy_map[c_r][c_c + 1] = candy_map[c_r][c_c + 1], candy_map[c_r][c_c]
                d = find_longest(c_r, c_r, c_c, c_c + 1)
                longest_candies = d if d > longest_candies else longest_candies
                candy_map[c_r][c_c], candy_map[c_r][c_c + 1] = candy_map[c_r][c_c + 1], candy_map[c_r][c_c]

    print(longest_candies)
    
if __name__ == "__main__":
    solution()
    