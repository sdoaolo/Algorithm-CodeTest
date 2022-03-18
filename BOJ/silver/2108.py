#2108_통계학_sort/implement_silver3
from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
li = []

for i in range(n):
    a= int(input())
    li.append(a)

li.sort()   

#산술평균 : N개의 수들의 합을 N으로 나눈 값
print(round(sum(li)/n))

#중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
print(li[n//2])

#최빈값 : N개의 수들 중 가장 많이 나타나는 값
#여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한
count = Counter(li).most_common(2)
if n>1:
    if count[0][1] == count[1][1]:
        print(count[1][0])
    else:
        print(count[0][0])
else:
    print(count[0][0])

#범위 : N개의 수들 중 최댓값과 최솟값의 차이
print(max(li)- min(li))