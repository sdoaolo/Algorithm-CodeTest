#2792_보석 상자_binary search_silver2
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
li = [int(input()) for _ in range(m)]

start = 1
end = max(li)
res = sys.maxsize

while(start<=end):
    mid = (start+end) // 2
    cnt = 0
    for i in li:
        if i % mid == 0:
            cnt += i // mid
        else:
            cnt += i// mid+1         
    
    if cnt > n: # 나눈 개수가 작은 것.. > 개수를 늘려주어도 된다 > mid가 커져도 된다 > start = mid+1
        start = mid +1
    else:
        end = mid - 1
        res = min(res, mid)
        
print(res) 