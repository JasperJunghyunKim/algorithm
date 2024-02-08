# push, pop, front, back,

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
        if self.empty():
            return -1
        else:
            return self.queue[-1]
    
    def push(self, number):
        self.queue.append(number)
            
    def pop(self):
        if self.empty():
            return -1
        else:
            front = self.queue[0]
            self.queue = self.queue[1:]
            return front
        
import sys
input = sys.stdin.readline

my_queue = Queue()

for _ in range(int(input())):
    command = input().strip().split()
    if command[0] == 'push':
        my_queue.push(command[1])
    elif command[0] == 'pop':
        print(my_queue.pop())
    elif command[0] == 'front':
        print(my_queue.front())
    elif command[0] == 'back':
        print(my_queue.back())
    elif command[0] == 'size':
        print(my_queue.size())
    elif command[0] == 'empty':
        print(my_queue.empty())