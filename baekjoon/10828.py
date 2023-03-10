from collections import deque
import sys

class Stack:
    def __init__(self, maxlen=10000):
        self.capacity = maxlen
        self.__stk = deque([], maxlen)
        
    def __len__(self):
        return len(self.__stk)
    
    def is_empty(self):
        return int(not self.__stk)
    
    def push(self, value):
        self.__stk.append(value)
    
    def pop(self):
        if self.is_empty():
            return -1
        return self.__stk.pop()
    
    def peek(self):
        if self.is_empty():
            return -1
        return self.__stk[-1]


stk = Stack()
N = int(sys.stdin.readline())
inputs = []

for _ in range(N):
    inputs.append(list(sys.stdin.readline().split()))

for input in inputs:
    if input[0] == 'push':
        stk.push(input[1])
    if input[0] == 'pop':
        print(stk.pop())
    if input[0] == 'size':
        print(stk.__len__())
    if input[0] == 'empty':
        print(stk.is_empty())
    if input[0] == 'top':
        print(stk.peek())

