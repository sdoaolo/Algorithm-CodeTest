# 11721_열 개씩 끊어 출력하기
n = input()
for i in range(len(n)//10+1):
    print(n[i*10:(i+1)*10])
