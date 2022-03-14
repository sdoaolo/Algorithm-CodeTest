# 2675_문자열 반복
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    r,s = input().split() 
    str = ""
    for c in s:
        str += c*int(r)
        
    print(str)
        