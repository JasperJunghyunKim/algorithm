from collections import deque

def solution(numbers, target ):
    answer = 0

    number_stack = deque()
    number_stack.append((numbers[0], 0, 0))
    number_stack.append((-numbers[0], 0, 0))

    while number_stack:
        cur_number, cur_index, cur_value = number_stack.pop()
        cur_value += cur_number
        if cur_index == len(numbers)-1:
            if cur_value == target:
                answer += 1
        else:
            number_stack.append((numbers[cur_index+1], cur_index+1, cur_value))
            number_stack.append((-numbers[cur_index+1], cur_index+1, cur_value))

    return answer

