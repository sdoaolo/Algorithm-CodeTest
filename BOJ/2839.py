#2839_설탕 배달

n = int(input())

c =0

while True:
    if n%5 == 0: #n이 5의 배수이면 5kg짜리 봉투로 나머지를 채우고 끝냄
        c += int(n//5)
        break
    n -= 3 #5의 배수가 아니면 일단 3개짜리를 빼준다. 
    c += 1 #봉투 개수 증가
    if n<0:
        c = -1
        break
    
print(c)