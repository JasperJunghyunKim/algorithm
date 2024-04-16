# import sys
# tc = int(sys.stdin.readline().strip())
# list_a = []
# for i in range(tc):
#     a, b = map(int, sys.stdin.readline().strip().split())
#     list_a.append(a+b)

# for i in list_a:
#     print(i)



import sys
n = int(sys.stdin.readline().strip())

list_a = [sum(map(int, sys.stdin.readline().strip().split())) for i in range(n)]

for i in list_a:
    print(i)