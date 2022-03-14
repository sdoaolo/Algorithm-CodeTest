# 에라토스테네스의 체를 이용한 풀이
# 소수 찾기

MAX = 1000000

check = [0] * (MAX+1)
check[0] = check[1] = True

for i in range(2, MAX+1):
    if not check[i] : # prime
        j = i+i 
        while j<=MAX:
            check[j] = True
            j+=i

m, n = map(int, input().split())

for i in range(m,n+1):
    if check[i] ==False:
        print(i)