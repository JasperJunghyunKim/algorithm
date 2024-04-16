########################################
# 23-12-15 (2)
# 에라토스테네스의 체
# https://coding-of-today.tistory.com/169
# https://coding-of-today.tistory.com/170
import math
def find_primes(num):
    array = [True for i in range(num + 1)]
    primes = []
    # for i in range(2, int(math.sqrt(num)) + 1):
    for i in range(2, num + 1):
        if array[i] == True:
            j = 2
            while i * j <= num:
                array[i * j] = False
                j += 1
    for i in range(2, num + 1):
        if array[i] == True:
            primes.append(i)
    return primes

a, b = map(int, input().strip().split(' '))
primes_a = find_primes(a)
primes_b = find_primes(b)
if a in primes_a:
    primes_a.remove(a)

print(*sorted(list(set(primes_b) - set(primes_a))), sep="\n")



# import math

# n = 1000	# 2부터 1000까지 모든 수에 대하여 소수를 찾을 것이다.
# array = [True for i in range(n + 1)] # 0,1을 제외한 모든 숫자가 소수(True)인 것으로 설정하고 시작한다.

# # 에라토스테네스의 체 알고리즘
# for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인
# 	if array[i] == True:	# i가 소수인 경우
#     	# i를 제외한 i의 모든 배수를 지우기
#         j = 2
#         while i * j <= n:
#         	array[i * j] = False
#             j += 1
            
# #모든 소수 출력
# for i range(2, n + 1):
# 	if array[i]:
#     	print(i, end = ' ')

########################################
# 23-12-15
import math
def is_prime(num):
    if num in [0, 1]: return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0: return False
    return True

a, b = map(int, input().strip().split(' '))
for i in range(a, b + 1):
    if is_prime(i): print(i)