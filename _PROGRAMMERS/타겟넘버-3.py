def solution(numbers, target):
    answer = 0
    
    stack = [] # [(val, index, sum), ]
    stack.append((numbers[0], 0, 0))
    stack.append((-numbers[0], 0, 0))
    
    while stack:
        cur_val, cur_index, cur_sum = stack.pop()
        cur_sum += cur_val
        
        if cur_index == len(numbers) - 1:
            if cur_sum == target:
                answer += 1
            continue
        
        next_index = cur_index + 1
        stack.append((numbers[next_index], next_index, cur_sum))
        stack.append((-numbers[next_index], next_index, cur_sum))
        
            
    return answer


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))