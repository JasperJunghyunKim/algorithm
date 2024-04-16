########################################
# 23-12-15 (2)
# 그리디로 도전


########################################
# 23-12-15 (1)
# 완전탐색으로 해결 - Permuations
import itertools

k = 80
dungeons = [[80,20],[50,40],[30,10]]

def solution(k, dungeons):
    answer = []
    cases = list(itertools.permutations(dungeons, len(dungeons)))
    for case in cases:
        cur_k = k
        cnt = 0
        for pre_k, use_k in case:
            if cur_k >= pre_k:
                cur_k -= use_k
                cnt += 1
        answer.append(cnt)
    return max(answer)

print(solution(k, dungeons))