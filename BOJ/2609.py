# 최대공약수와 최소공배수

def gcd (x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)
    
x, y = map(int,input().split())

ans = gcd(x,y)
print(ans)
print(x*y//ans)