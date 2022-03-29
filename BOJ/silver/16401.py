#16401_과자나눠주기_binary search_silver3

import sys
input = sys.stdin.readline

m , n = map(int,input().split())
snack = list(map(int,input().split()))

start = 1
end = max(snack)
res = 0

while start <= end:
    cnt = 0
    mid = (start+end) //2
    
    if mid == 0:
        cnt = 0
        break
    #filteredSnack 은 mid 값보다 길이가 긴 리스트
    filteredSnack = list(filter(lambda x: x>=mid, snack))
    for s in filteredSnack: 
        cnt += s // mid # 과자 길이를 중간값(현재 잘라볼 길이)으로 나누면 
                        # 몫의 개수가 그 과자에서 나올수 있는 개수임
        
    #start가 mid+1 이 되면 이후 mid값이 커지므로 > cnt개수가 적어짐!
    #총 개수가 m보다 크면 start 재설정
    if cnt >= m:
        start = mid + 1
        res = mid
    
    # 총개수가 m보다 작으면 더 많이 필요한것이고
    # end를 mid -1 롤 설정 시 이후 mid 값이 작아지므로 > cnt개수가 많아짐!
    else: end = mid - 1
    
print(res)
    
    