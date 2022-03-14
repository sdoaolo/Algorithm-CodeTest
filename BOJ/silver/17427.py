# 약수의합 시간 복잡도 계산하는 과정 매우 중요함!!! 이건 다시 공부하기

n = int(input())
ans = 0

for i in range(1,n+1):
    ans += i * (n//i)
print(ans)