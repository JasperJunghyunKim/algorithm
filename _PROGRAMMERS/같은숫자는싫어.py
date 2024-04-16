def solution(arr):
    
    l = [arr[0]]
    for n in arr[1:]:
        if n != l[-1]: l.append(n)
    return l

if __name__ == "__main__":
    arr = [1,1,3,3,0,1,1]
    # arr = [4,4,4,3,3]
    print(solution(arr))