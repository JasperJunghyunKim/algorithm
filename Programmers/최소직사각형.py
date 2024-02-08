########################################
# 다른 사람 풀이 참고
# 결과는 (큰 것 중 최대 * 작은 것 중 최대) 이므로 min max 를 잘 활용
def solution(sizes):
    return max([min(x) for x in sizes]) * max([max(x) for x in sizes])

########################################
# 23-12-15

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]	

def solution(sizes):
    for size in sizes:
        if size[0]> size[1]: continue
        else:
            temp = size[0]
            size[0] = size[1]
            size[1] = temp

    print(sizes)

    max_a, max_b = 0, 0
    for size in sizes:
        if size[0] > max_a: max_a = size[0]
        if size[1] > max_b: max_b = size[1]
    return max_a * max_b

print(solution(sizes))