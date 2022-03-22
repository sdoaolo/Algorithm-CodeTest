#10866_덱_data structure_silver4
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
deq = deque()

for i in range(n):
    comm = input().rstrip()
    if len(comm) >= 10:
        comm, x = comm.split()    
        
    l = len(deq)
    
    if comm == "push_front":
        deq.appendleft(x)

    elif comm == "push_back":
        deq.append(x)

    elif comm == "pop_front":
        if l == 0:
            print(-1)
        else:
            print(deq.popleft())
            
    elif comm == "pop_back":
        if l == 0:
            print(-1)
        else:
            print(deq.pop())
        
    elif comm == "size":
        print(l)
        
    elif comm == "empty":
        if l == 0:
            print(1)
        else:
            print(0)
            
    elif comm == "front":
        if l == 0:
            print(-1)
        else:
            print(deq[0])
        
    elif comm == "back":
        if l == 0:
            print(-1)
        else:
            print(deq[-1])
            
