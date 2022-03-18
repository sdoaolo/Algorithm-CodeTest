#1439_뒤집기_greedy_silver5
import sys
s = sys.stdin.readline().rstrip()
l = len(s)

zero, one = 0,0
if s[0] == '0':
    zero+=1
else:
    one+=1

for i in range(1, l):
    if s[i] != s[i-1]:
        if s[i] == '0':
            zero+=1
        else:one+=1

print(min(zero,one))