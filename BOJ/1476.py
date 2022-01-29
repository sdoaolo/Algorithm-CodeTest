#1476 날짜계산

e,s,m = map(int,input().split())

E,S,M = 1,1,1
year = 1

while True:
    if E ==e and S == s and M == m:
        print(year)
        break
    E +=1
    S +=1
    M +=1
    if E == 16:
        E = 1
    if S == 29:
        S = 1
    if M == 20:
        M = 1
        
    year+=1