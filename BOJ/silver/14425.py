#14425_문자열 집합
import sys
input = sys.stdin.readline
n,m = map(int, input().split())

s = set()
for i in range(n):
    s.add(input().rstrip())

res = 0
for k in range(m):
    if input().rstrip() in s:
       res+=1 
       
print(res)