import time
numbers = [i for i in range(1, 21)]
number_check = [False for _ in range(20)]
LEN_NUMBERS = len(numbers)

def combination(cnt, r, idx):
    global g_cnt
    global g_test_summation
    if cnt == r:
        for i in range(LEN_NUMBERS):
            if number_check[i]: g_test_summation += numbers[i]
        g_cnt += 1
        return
    for i in range(idx, LEN_NUMBERS):
        number_check[i] = True
        combination(cnt + 1, r, i + 1)
        number_check[i] = False
     
def combination2(l, cnt, r, idx):
    global g_cnt
    global g_test_summation
    if cnt == r:
        for i in l:
            g_test_summation += i
        g_cnt += 1
        return
    for i in range(idx, LEN_NUMBERS):
        combination2(l + [numbers[i]], cnt + 1, r, i + 1)
        
def combination3(l, cnt, r, idx):
    global g_cnt
    global g_test_summation
    if cnt == r:
        for i in l:
            g_test_summation += i
        g_cnt += 1
        return
    for i in range(idx, LEN_NUMBERS):
        nl = l[::]
        nl.append(numbers[i])
        combination3(nl, cnt + 1, r, i + 1)
        

        

g_cnt = 1
g_test_summation = 0
start_time = time.time()   
combination(0, 9, 0)
print("combination 1 : Using Boolean Check List")
print(g_test_summation)
print(g_cnt)
print(time.time() - start_time)


g_cnt = 1
g_test_summation = 0
start_time = time.time()   
combination2([], 0, 9, 0)
print("combination 2 : By adding an item directly to new list")
print(g_test_summation)
print(g_cnt)
print(time.time() - start_time)


g_cnt = 1
g_test_summation = 0
start_time = time.time()   
combination3([], 0, 9, 0)
print("combination 3 : By adding an item using append method to new list")
print(g_test_summation)
print(g_cnt)
print(time.time() - start_time)
