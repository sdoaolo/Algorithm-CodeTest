#1316 다시풀기

import sys
n = int(input())
answer = 0

for i in range(n):
    s =  sys.stdin.readline().rstrip()
    sl = len(s)
    for k in range(sl):
        if k != sl-1:
            if s[k] == s[k+1]:
                pass
            elif s[k] in s[k+1:]:
                break
        else:
            answer +=1
            
print(answer)