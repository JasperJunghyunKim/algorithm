
# https://somjang.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%98%EB%8A%94-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%8A%A4%ED%83%9D-Stack

########################################
# 23-12-14
import sys
sys_input = sys.stdin.readline
from collections import deque

num_cmd = int(sys_input())
stack = deque()
for _ in range(num_cmd):
    cmd = list(sys_input().strip().split(' '))
    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(stack) == 0: print(-1)
        else:
            print(stack.pop())
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        if len(stack) == 0 : print(1)
        else : print(0)
    elif cmd[0] == 'top':
        if len(stack) == 0: print(-1)
        else:
            print(stack[-1])


########################################
# 23-11
# Class 사용
class Stack():
    def __init__(self) -> None:
        self.stack = []
    
    def isEmpty(self):
        is_empty = 0
        if len(self.stack) == 0:
            is_empty = 1
        return is_empty

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        pop_object = None
        if self.isEmpty():
            pop_object = -1
        else:
            pop_object = self.stack.pop()
        return pop_object
    
    def top(self):
        top_object = None
        if self.isEmpty():
            top_object = -1
        else:
            top_object = self.stack[-1]
        return top_object
    
    def size(self):
        return len(self.stack)
    
import sys
n = int(sys.stdin.readline())
my_stack = Stack()
for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        my_stack.push(int(command[1]))
    elif command[0] == 'pop':
        print(my_stack.pop())
    elif command[0] == 'size':
        print(my_stack.size())
    elif command[0] == 'empty':
        print(my_stack.isEmpty())
    elif command[0] == 'top':
        print(my_stack.top())