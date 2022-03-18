#1543_문서검색_greedy_silver4

import sys
input = sys.stdin.readline
m = input().rstrip()
search = input().rstrip()
lm = len(m)
ls = len(search)
i, res =0,0
while i <= lm:
    if m[i:i+ls] == search:
        i = i+ls
        res+=1
    else:
        i+=1
        
print(res)