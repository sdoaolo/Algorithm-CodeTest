#2343_기타 레슨_binary search_silver1_다시ㅎ

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int,input().split()))

start = max(li) #전체 강의가 블루레이에 들어가려면, 가장 큰 분이 최소단위가 되어야함
end = sum(li) #다 합친 것보다 클 수 없음

while start <= end:
    mid = (start+end) //2
    hap = 0
    cnt = 1

    for i in range(n):
        hap += li[i]
        if hap > mid : 
            cnt += 1
            hap = li[i]

    # 블루레이 개수가 m보다 크면 더 적게 만들어야 하는데 (각 크기가 작은것)
    # start를 키우면 mid가 커지므로 > 각 블루레이의 크기가 커집 > 블루레이 개수 적어짐
    if cnt > m:
        start = mid + 1
    else:
        res = mid
        end = mid - 1
        
        
print(res)