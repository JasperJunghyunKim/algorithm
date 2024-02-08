########################################
# 23-12-15

answers = [1,3,2,4,2]

def solution(answers):
    answer = []
    supo_1 = [1, 2, 3, 4, 5]
    supo_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    num_corrects = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == supo_1[i%5]:
            num_corrects[0] += 1
        if answers[i] == supo_2[i%8]:
            num_corrects[1] += 1
        if answers[i] == supo_3[i%10]:
            num_corrects[2] += 1
    max_score = max(num_corrects)
    for i, v in enumerate(num_corrects):
        if max_score == v:
            answer.append(i+1)
    return sorted(answer)

print(solution(answers))