########################################
# T2

import sys
input = sys.stdin.readline

l_string = list(input().strip())
r_string = list()

for _ in range(int(input())):
    command = input().strip()
    if command[0] == 'L':
        if l_string:
            r_string.append(l_string.pop())
    elif command[0] == 'D':
        if r_string:
            l_string.append(r_string.pop())
    elif command[0] == 'B':
        if l_string:
            l_string.pop()
    elif command[0] == 'P':
        l_string.append(command[2])

r_string.reverse()
print(''.join(l_string) + ''.join(r_string))

# ########################################
# # T1 시간초과
# # insert 는 O(n) 이며, O(1) 인 append, pop 보다 시간복잡도가 높음
# import sys
# input = sys.stdin.readline

# string = input().strip()
# cur_index = len(string)
# num_commands = int(input())

# for i in range(num_commands):
#     command = input().strip()
#     if command[0] == 'L':
#         if cur_index == 0:
#             continue
#         else:
#             cur_index -= 1
#     elif command[0] == 'D':
#         if cur_index == len(string):
#             continue
#         else:
#             cur_index += 1
#     elif command[0] == 'B':
#         if cur_index == 0:
#             continue
#         else:
#             string = string[0:cur_index-1] + string[cur_index:]
#             cur_index -= 1
#     elif command[0] == 'P':
#         string = string[0:cur_index].strip() + command[2].strip() + string[cur_index:].strip()
#         cur_index += 1

# print(string)