#1463_1로 만들기

# 공부 다시해도 기억 잘 안날듯 ㅠ

import sys
input = sys.stdin.readline
n = int(input())

d = [0]* 1000001

for i in range(2,n+1):
    d[i] = d[i-1]+ 1
    if i %2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i%3 == 0:
        d[i] = min(d[i],d[i//3]+1)
    
    print(i," i : d[i] ",d[i])

print(d[n])