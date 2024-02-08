# participant = ["mislav", "stanko", "mislav", "ana"]	
# completion = ["stanko", "ana", "mislav"]

participant = ["leo", "kiki", "eden"]	
completion = ["eden", "kiki"]	

########################################
# 2. 해시
########################################
def solution(participant, completion):
    hash_map = dict()
     
    for runner in participant:
        if hash_map.get(runner) == None: hash_map.update({runner:0})
        hash_map[runner] += 1

    for runner in completion:
        hash_map[runner] -= 1

    for k, v in hash_map.items():
        if v == 1: return k

print(solution(participant, completion))

# ########################################
# # 1. sort + for 해결
# ########################################

# def solution(participant, completion):
#     answer = ''
#     participant.sort()
#     completion.sort()
#     for runner1, runner2 in zip(participant, completion):
#         if runner1 != runner2:
#             return runner1
#     else:
#         return participant[-1]

# print(solution(participant, completion))