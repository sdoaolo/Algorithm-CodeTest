#10828_스택
import sys
input = sys.stdin.readline
n = int(input())

stack = []
for _ in range(n):
    length = len(stack)
    com = input().rstrip()
    if len(com) >= 6: # push
        com, x = com[:4],com[5:]
        stack.append(x)
    elif com == "pop":
        if length != 0: 
            print(stack.pop())
        else:
            print(-1)
    elif com == "size":
        print(length)
    elif com == "empty":
        if length == 0:
            print(1)
        else: print(0)       
    elif com == "top":
        if length != 0: 
            print(stack[length-1])
        else: print(-1)
    