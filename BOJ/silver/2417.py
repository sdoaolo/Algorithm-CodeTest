#2417_정수제곱근_binary search_silver4
import sys
input = sys.stdin.readline

n = int(input())
start, end = 0, n
res = n
while start <= end:
    mid = (start+end) // 2 #mid를 제곱근이라 가정
        
    if mid**2 >= n: #n보다 크면 end값을 줄여야함.
        res = min(res,mid)
        end = mid-1 
    else:
        start = mid +1

print(res)