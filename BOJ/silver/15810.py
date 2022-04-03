#15810_풍선 공장_binary search_silver2

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
li = list(map(int,input().split()))

li.sort()

start = 1
end = 1000000 **2

res = end

while(start <= end):
    mid = (start+end)//2
    
    #1개 풍선 만드는 사람이 mid 시간동안 만드는 풍선의 개수 >> 총인원의 합
    cnt = sum(mid // x for x in li)
     
    if cnt >= m: #풍선의 개수가 많거나 같으면 cnt를 줄여야함 > mid 값이 작아지면 cnt도 작아짐.
        end = mid -1
        res = min(res,mid)
        
    else: #풍선의 개수가 작으면 더 만들어야 하므로 > cnt가 늘어나기 위해선 mid 값이 커져야함 >>> start = mid +1
        start = mid+1
    
print(res)