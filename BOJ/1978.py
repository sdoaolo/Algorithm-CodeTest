# 소수 찾기

def prime(n):
    if(n<2):
        return False
    i=2
    while i*i <=n:
        if n % i ==0:
            return False
        i+=1
    return True
    
n = int(input())
li = list(map(int, input().split()))

ans = 0
for i in li:
    if prime(i):
        ans+=1
        
print(ans) 