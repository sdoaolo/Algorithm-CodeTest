#2776_암기왕_sort_silver4
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    set1 = set(map(int,input().split()))
    m = int(input())
    set2 = list(map(int,input().split()))
    
    for i in set2:
        if i in set1:
            print(1)
        else:
            print(0)