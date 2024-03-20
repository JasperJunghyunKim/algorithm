from collections import deque
l = deque([1,2,3,4,5,6,7])
l = deque(list(l)[3:])
print(l)