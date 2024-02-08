########################################
# t2 : 직접구현
########################################
def solution(nums):
    hash_list = list()
    for species in nums:
        if species in hash_list : continue
        else: hash_list.append(species)

    if len(hash_list) >= len(nums)//2 : return len(nums)//2
    else: return len(hash_list)

# ########################################
# # t1 : set 사용
# ########################################
def solution(nums):
    half = len(nums)/2
    num_set = set(nums)
    if len(num_set) >= half: return half
    else: return len(num_set)