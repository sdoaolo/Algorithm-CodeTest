#4158_CD_binary search_silver5
import sys
input = sys.stdin.readline

while(1):   
    n, m = map(int,input().split())
    if (n,m) == (0,0):
        break
    
    sk = [int(input()) for _ in range(n)]
    sy = [int(input()) for _ in range(m)]
    
    res = 0
    
    #sy의 값을 하나씩 탐색 
    for cdNum in sy:
        start, end = 0, n-1
        while start <=end:
            mid = (start+end) // 2
            
            if sk[mid] == cdNum: 
                res+=1
                break
            elif sk[mid] > cdNum:
                # 값이 크면 왼쪽에 있는것 이므로  
                end = mid-1
            elif sk[mid] < cdNum:
                start = mid+1

    print(res)
    
    


