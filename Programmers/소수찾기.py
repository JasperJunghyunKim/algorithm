########################################
# 23-12-15 (2)
import itertools
import math

def is_prime(number):
    if number <= 1: return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0: return False
    return True

def find_permuations(array):
    temp1 = []
    temp2 = []
    for i in range(1, len(array) + 1):
        temp1.extend(list(itertools.permutations(array, i)))
    for numbers in temp1:
        temp_num = ""
        for i in numbers:
            temp_num += str(i)
        temp_num = int(temp_num)
        temp2.append(temp_num)
    temp2 = list(set(temp2))
    return temp2

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    numbers = find_permuations(numbers)
    for number in numbers:
        if is_prime(number) : answer += 1
    return answer

print(solution([1,2,3]))

# ########################################
# # 23-12-15 (1)

# import itertools
# import math

# numbers = [1,1,0]

# def make_candidates(numbers):
#     raw_candidates = []
#     candidates = []
#     for i in range(1, len(numbers) + 1):
#         raw_candidates.extend(list(itertools.permutations(numbers, i)))
#     for numbers in raw_candidates:
#         number = ""
#         for i in numbers:
#             number += str(i)
#         candidates.append(number)
#     candidates = list(map(int, candidates))
#     candidates = list(set(candidates))
#     return candidates
   

# def is_prime(number):
#     if number == 1 or number == 0:
#         return False
#     for i in range(2, int(math.sqrt(number) + 1)):
#         if number % i == 0: 
#             return False
#     return True

# def solution(numbers):
#     answer = 0
#     numbers = list(numbers)

#     candidates = make_candidates(numbers)
#     for number in candidates:
#         if is_prime(number): answer += 1
#     return answer

# print(solution(numbers))