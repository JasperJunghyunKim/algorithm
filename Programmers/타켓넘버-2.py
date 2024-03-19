#
# 24-03-18
# DFS(Recursive)
#

def solution(numbers, target):
    answer = [0]
    max_index = len(numbers) - 1
    
    def recursive(index, tmp_sum):
    
        if index == max_index:
            if tmp_sum + numbers[index]  == target:
                answer[0] += 1
            if tmp_sum - numbers[index] == target:
                answer[0] += 1
            return
        
        # add
        recursive(index + 1, tmp_sum + numbers[index])
        
        # sub
        recursive(index + 1, tmp_sum - numbers[index])
    
    recursive(0, 0)
    
    return answer[0]