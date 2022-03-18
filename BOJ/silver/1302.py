#1302_베스트셀러_string_silver3
from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
    li.append(input().rstrip())
    
count = Counter(li).most_common()
maxNum = count[0][1]
res = []
l = len(count)

for i in range(l):
    if maxNum == count[i][1]:
        res.append(count[i][0])
    
res.sort()
print(res[0])