import time
import random
import psutil
SIZE = 20_000
g_mem = 0

# sample_list = [i for i in range(SIZE)]
sample_list = random.sample(range(SIZE), SIZE)

# memory check
def mem_usage():
    p = psutil.Process()
    #byte를 사람이 인지하기 쉬운 megabyte로 변환
    #megabyte이므로 1024 * 1024의 값을 나눠줌
    return p.memory_info().rss

# CASE 1
# 새 리스트인 [item] 을 case_1 에 더하는 방식으로 case_1 에 할당함
# 이 과정에서 [item] 이라는 중간 객체가 생성되므로, 메모리 사용량이 급격히 증가함
def f1():
    global g_mem
    case_1 = []
    start_time = time.time()
    for item in sample_list:
        case_1 = case_1 + [item]
    print("CASE 1 TIME : ", time.time() - start_time)
    print("CASE 1 MEM : ", mem_usage() - g_mem, " BYTES")
    print()

# CASE 2
# += 연산자로 [item] 을 in-place 로 추가
# 메모리 재할당이 발생하지만, 중간 객체가 생성되지 않으으로 CASE1 보다 메모리 효율이 높음
def f2():
    case_2 = []
    start_time = time.time()
    for item in sample_list:
        case_2 += [item]
    print("CASE 2 TIME : ", time.time() - start_time)
    print("CASE 2 MEM : ", mem_usage() - g_mem, " BYTES")
    print()

    

# CASE 3
# in-place 로 추가
# CASE2 와 마찬가지로 재할당만 발생
def f3():
    case_3 = []
    start_time = time.time()
    for item in sample_list:
        case_3.append(item)
    print("CASE 3 TIME : ", time.time() - start_time)
    print("CASE 3 MEM : ", mem_usage() - g_mem, " BYTES")
    print()

# CASE 4
# CASE3 의 append 라는 메서드를 호출하는 오버헤드를 줄이고자 했으나, 겨로가적으로 큰 차이 나지 않음
# 메모리적으로도 CASE3와 차이나지 않음
def f4():
    case_4 = []
    start_time = time.time()
    append_to_4 = case_4.append
    for item in sample_list:
        append_to_4(item)
    print("TEST CASE 4 : ", time.time() - start_time)
    print("CASE 4 MEM : ", mem_usage() - g_mem, " BYTES")
    print()

# CASE 5
# 미리 큰 메모리를 할당하므로, 재할당은 발생하지 않음
# 초기 메모리 사용량이 큼
def f5():
    case_5 = [1 for _ in range(SIZE)]
    start_time = time.time()
    for i, v in enumerate(sample_list):
        case_5[i] = sample_list[i]
    print("TEST CASE 5 : ", time.time() - start_time)
    print("CASE 5 MEM : ", mem_usage() - g_mem, " BYTES")
    print()

g_mem = mem_usage()
f1()
g_mem = mem_usage()
f2()
g_mem = mem_usage()
f3()
g_mem = mem_usage()
f4()
g_mem = mem_usage()
f5()