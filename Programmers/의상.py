clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
def solution(clothes):
    answer = 1
    clothes_dict = dict()
    for wear, category in clothes:
        if clothes_dict.get(category) == None: clothes_dict.update({category : []})
        clothes_dict.get(category).append(wear)
    
    for i in clothes_dict.values():
        answer *= (len(i)+1)
    return answer-1

print(solution(clothes))
