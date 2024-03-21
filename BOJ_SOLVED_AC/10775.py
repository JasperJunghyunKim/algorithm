import sys
sys_input = sys.stdin. readline

num_gates = int(sys_input())
num_planes = int(sys_input())
dock_list = [int(sys_input()) for _ in range(num_planes)]
reserved = [i for i in range(num_gates+1)]


for i in dock_list:
    for j in range(1, i+1):
        