########################################
# T2 : left_arr, right_arr 를 할당하여 메모리를 낭비하지 않고 기존 arr 그대로 사용
########################################
def divide_and_sort(arr, low, high):
    if low < high:
        mid = (low + high)//2
        divide_and_sort(arr, low, mid)
        divide_and_sort(arr, mid+1, high)
        merge(arr, low, mid, high)
    return

def merge(arr, low, mid, high):
    i = low
    j = mid + 1
    temp = []
    while i <= mid and j <= high:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    while i <= mid:
        temp.append(arr[i])
        i += 1
    while j <= high:
        temp.append(arr[j])
        j += 1
    i = low
    for n in temp:
        arr[i] = n
        i += 1
    return 

# MAIN
arr = [6,7,8,3,4,5,0,1,2,9]
divide_and_sort(arr, 0, len(arr)-1)
print(arr)


# ########################################
# # T1 : 직관적이지만 병합할 때 마다 메모리가 낭비됨
# # 참조 : https://www.daleseo.com/sort-merge/
# ########################################
# def merge_sort(arr):
#     if len(arr) < 2:
#         return arr
#     else:
#         mid = len(arr)//2

#         l_arr = merge_sort(arr[:mid])
#         r_arr = merge_sort(arr[mid:])
        
#         merged_arr = []
#         i = j = 0
#         while i < len(l_arr) and j < len(r_arr):
#             if l_arr[i] < r_arr[j]:
#                 merged_arr.append(l_arr[i])
#                 i += 1
#             else:
#                 merged_arr.append(r_arr[j])
#                 j += 1
#         merged_arr.extend(l_arr[i:])
#         merged_arr.extend(r_arr[j:])
#         return merged_arr
    
# # MAIN
# arr = [6,7,8,3,4,5,0,1,2,9]
# arr = merge_sort(arr)
# print(arr)
        