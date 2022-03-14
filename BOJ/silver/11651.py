#11651_좌표 정렬하기 2
import sys
input = sys.stdin.readline
n = int(input())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))
    
li.sort(key = lambda x :(x[1],x[0]))

for x, y in li:
    print(f"{x} {y}")