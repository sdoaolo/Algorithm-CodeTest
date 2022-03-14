#10987_모음의 개수

import sys
input = sys.stdin.readline

s = input().rstrip()

li = ['a','e','i','o','u']

res=0
for i in li:
    res+=s.count(i)
        
print(res)