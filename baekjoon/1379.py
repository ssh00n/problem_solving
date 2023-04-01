import sys
import heapq
input = sys.stdin.readline


n = int(input())
lectures = []
for _ in range(n):
    no, start, end = map(int, input().split())
    lectures.append((no, start, end))

lectures.sort(key=lambda x: (x[1], x[2], x[0]))

count = 1

cno, cstart, cend = lectures[0]

classrooms = []
heapq.heappush(classrooms, (cend, 1))

cinfo = [0] * (n + 1)
cinfo[cno] = 1

for i, lecture in enumerate(lectures[1:]):
    no, start, end = lecture
    classend, classno = classrooms[0]
    
    if classend <= start:
        heapq.heappop(classrooms)
        heapq.heappush(classrooms, (end, classno))
        cinfo[no] = classno
    else:
        count += 1
        heapq.heappush(classrooms, (end, count))
        cinfo[no] = count
        
print(count)

for c in cinfo[1:]:
    print(c)