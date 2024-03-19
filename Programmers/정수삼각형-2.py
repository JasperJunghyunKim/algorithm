#
# 24-03-19
# Top Down
#

def solution(triangle):

    tri_height = len(triangle)    
    dp = [[-1 for _ in range(tri_height)] for _ in range(tri_height)]

    def find_max(height, index):
        
        if dp[height][index] != -1: 
            return dp[height][index]
        else:              
            if height == 0:
                dp[height][index] = triangle[height][index]
            elif index == 0:
                dp[height][index] = find_max(height - 1, index) + triangle[height][index]
            elif index == height:
                dp[height][index] = find_max(height - 1, index - 1) + triangle[height][index]
            else:
                dp[height][index] = max(find_max(height - 1, index - 1), find_max(height - 1, index)) + triangle[height][index]
            return dp[height][index]
           
    # 삼각형 아랫변 
    for idx in range(tri_height):
        find_max(tri_height - 1, idx)
    
    return max(dp[tri_height - 1])