from collections import deque
import sys

class Queue:
    def __init__(self, maxlen=2000001):
        self.capacity = maxlen
        self.__que = deque([], maxlen)
        self.size = 0

    def __len__(self):
        return len(self.__que)
    
    def is_empty(self):
        return int(not self.__que)
    
    def push(self, value):
        self.__que.append(value)
    
    def pop(self):
        if self.is_empty():
            return -1
        return self.__que.popleft()
    
    def front(self):
        if self.is_empty():
            return -1
        else:
            return self.__que[0]
    
    def back(self):
        if self.is_empty():
            return -1
        else:
            return self.__que[-1]
    
que = Queue()
N = int(sys.stdin.readline())
inputs = []

for _ in range(N):
    inputs.append(list(sys.stdin.readline().split()))

for input in inputs:
    if input[0] == 'push':
        que.push(input[1])
    if input[0] == 'pop':
        print(que.pop())
    if input[0] == 'size':
        print(que.__len__())
    if input[0] == 'empty':
        print(que.is_empty())
    if input[0] == 'front':
        print(que.front())
    if input[0] == 'back':
        print(que.back())
