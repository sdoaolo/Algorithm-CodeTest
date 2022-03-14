#2512_예산
import sys
input =sys.stdin.readline
n = int(input())
li = list(map(int, input().split()))
all = int(input())

start, end = 0, max(li)

while start <=end:
        mid = (start+end)//2
        hap = 0
        for i in range(n):
            if mid <= li[i]:
                hap+=mid
            else:
                hap+= li[i]
                
        if hap <= all: start = mid+1
        else: end = mid -1
        
print(end)