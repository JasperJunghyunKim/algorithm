########################################
# T2 : 
########################################
import sys
input = sys.stdin.readline

size_arr, k = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
saved_history = []

def merge_sort(arr, min_i, max_i):
    if min_i < max_i:
        mid_i = (min_i + max_i)//2
        merge_sort(arr, min_i, mid_i)
        merge_sort(arr, mid_i + 1, max_i)
        merge(arr, min_i, mid_i, max_i)

def merge(arr, min_i, mid_i, max_i):
    i = min_i
    j = mid_i + 1
    temp = []
    while i <= mid_i and j <= max_i:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            saved_history.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            saved_history.append(arr[j])
            j += 1
    while i <= mid_i:
        temp.append(arr[i])
        saved_history.append(arr[i])
        i += 1
    while j <= max_i:
        temp.append(arr[j])
        saved_history.append(arr[j])
        j += 1
    i = min_i
    for n in temp:
        arr[i] = n
        i += 1

# MAIN
merge_sort(arr, 0, len(arr)-1)
if len(saved_history) < k:
    print(-1)
else:
    print(saved_history[k-1])

# ########################################
# # T1 : 문제에 나온 수도코드로 풀지 않아서 틀렸음 (방법자체가 머지 소트에 틀린 건 아님)
# ########################################
# import sys
# input = sys.stdin.readline

# size_arr, k = map(int, input().split(' '))
# arr = list(map(int, input().split(' ')))
# saved_history = []

# def merge_sort(arr):
#     global cnt
#     if len(arr) < 2:
#         return arr
#     else:
#         mid = len(arr)//2
#         left_arr = merge_sort(arr[:mid])
#         right_arr = merge_sort(arr[mid:])
        
#         # MERGE
#         i = j = 0
#         merged_arr = []
#         while i < len(left_arr) and j < len(right_arr):
#             if left_arr[i] < right_arr[j]:
#                 merged_arr.append(left_arr[i])
#                 saved_history.append(left_arr[i])
#                 i += 1
#             else:
#                 merged_arr.append(right_arr[j])
#                 saved_history.append(right_arr[j])
#                 j += 1
#         for m in left_arr[i:]:
#             merged_arr.append(m)
#             saved_history.append(m)
#         for n in right_arr[j:]:
#             merged_arr.append(n)
#             saved_history.append(n)

#         return merged_arr
        
# # MAIN
# arr = merge_sort(arr)

# if len(saved_history) < k:
#     print(-1)
# else:
#     print(saved_history[k-1])