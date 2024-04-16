import math

brown =24
yellow = 24

def solution(brown, yellow):
    answer = []

    for i in range(1, int(math.sqrt(yellow)) + 2):
        if yellow % i == 0:
            width = i
            height = yellow // i
            if ((width + 2) + height) * 2 == brown:
                width = width + 2
                height = height + 2
                answer = sorted([height, width], reverse=True)
                break
    return answer

print(solution(brown, yellow))