#10250_ACM 호텔_implement_bronze3
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    h,w,n = map(int,input().split())
    #호텔의 층수, 각층의 방수, 몇번째 손님
    
    if n % h == 0:
        mok = n//h
        namuji = h
    else:
        mok = n//h + 1 #몫이 1이면 > 방번호는 2까지 이동한다는 뜻
        namuji = n%h # 방의 층
    
    mok ,namuji= str(mok), str(namuji)    
    
    #나머지의 개수만큼
    if len(str(mok)) == 1:
        mok = "0" +str(mok)
    res = namuji + mok
    print(res)
    