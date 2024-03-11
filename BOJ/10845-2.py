#
# 24-03-11
# Class
#

class Queue():
    def __init__(self) -> None:
        self.queue = []
        
    def size(self):
        return len(self.queue)
    
    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0
    
    def front(self):
        if self.empty():
            return -1
        else:
            return self.queue[0]
        
    def back(self):
        if self.empty() == 1:
            return -1
        else:
            return self.queue[-1]
        
    def push(self, n):
        self.queue.append(n)
        
    def pop(self):
        if self.empty():
            return -1
        else:
            tmp = self.queue[0]
            self.queue = self.queue[1:]
            return tmp
        
import sys
input = sys.stdin.readline

n = int(input())

my_queue = Queue()

for i in range(n):
    cmd = input().strip().split()
    if cmd[0] == 'push': my_queue.push(int(cmd[1]))
    elif cmd[0] == 'pop': print(my_queue.pop())
    elif cmd[0] == 'size': print(my_queue.size())
    elif cmd[0] == 'empty': print(my_queue.empty())
    elif cmd[0] == 'front': print(my_queue.front())
    elif cmd[0] == 'back': print(my_queue.back())