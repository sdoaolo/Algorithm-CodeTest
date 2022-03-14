#16561_3의 배수

import sys
input = sys.stdin.readline

n = int(input())

res = 1
c = 2

for i in range(9,n,3):
    res += c
    c+=1
    
print(res)