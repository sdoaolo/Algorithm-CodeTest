#1436_영화감독 숌_brute force_ silver5

n = int(input())
num = 666
res=[]
while len(res) < n: #n개 채워지면 종료
    if '666' in str(num):
        res.append(num)
    num += 1

#n번째 데이터 출력
print(res[n-1]) 