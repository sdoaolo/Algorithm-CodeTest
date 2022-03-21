#20291_파일 정리_string_silver3
import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
    filename, fileExtension = input().rstrip().split('.')
    li.append(fileExtension)

c = Counter(li)
li = sorted(c.items())
for i in range(len(li)):
    print(f"{li[i][0]} {li[i][1]}")