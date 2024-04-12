import time
LEN_NUM = 30
R = 15
numbers = [i for i in range(LEN_NUM)]

g_comb1_sum = 0
g_comb2_sum = 0
g_comb3_sum = 0
g_comb1_cnt = 0
g_comb2_cnt = 0
g_comb3_cnt = 0

selected = [False] * LEN_NUM
def combination1(length, r, idx):
    global g_comb1_sum
    global g_comb1_cnt
    if length == r:
        g_comb1_cnt += 1
        for i in range(LEN_NUM):
            if selected[i]:
                g_comb1_sum += numbers[i]
        return
    for i in range(idx, LEN_NUM):
        selected[i] = True
        combination1(length + 1, r, i + 1)
        selected[i] = False

time_before = time.time()
print("COMBINATION 1")
combination1(0, R, 0)
print("SUM : ", g_comb1_sum)
print("CNT : ", g_comb1_cnt)
print("TIME : ", time.time() - time_before)

def combination2(comb_list, length, r, idx):
    global g_comb2_sum
    global g_comb2_cnt
    if length == r:
        g_comb2_cnt += 1
        for i in comb_list:
            g_comb2_sum += i
        return
    for i in range(idx, LEN_NUM):
        combination2(comb_list + [numbers[i]], length + 1, r, i + 1)

time_before = time.time()
print("COMBINATION 2")
combination2([], 0, R, 0)
print("SUM : ", g_comb2_sum)
print("CNT : ", g_comb2_cnt)
print("TIME : ", time.time() - time_before)

def combination3(comb_list, length, r, idx):
    global g_comb3_sum
    global g_comb3_cnt
    if length == r:
        g_comb3_cnt += 1
        for i in comb_list:
            g_comb3_sum += i
        return
    for i in range(idx, LEN_NUM):
        comb_list.append(numbers[i])
        combination3(comb_list, length + 1, r, i + 1)
        comb_list.pop()

time_before = time.time()
print("COMBINATION 3")
combination3([], 0, R, 0)
print("SUM : ", g_comb3_sum)
print("CNT : ", g_comb3_cnt)
print("TIME : ", time.time() - time_before)