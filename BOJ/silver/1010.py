#다리 놓기

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    res = factorial(m) //(factorial(m - n) * factorial(n))
    print(res)