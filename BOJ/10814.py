#10814 나이순 정렬

#나이순, 나이가 같으면 가입한 순(입력이 가입한 순서로 주어짐)
n = int(input())

li = []
for i in range(n):
    age , name = map(str,input().split())
    li.append((int(age),name))
    
li.sort(key=lambda x:x[0])  
# lambda : 익명함수 지칭하여 바로 정의해 사용하는 함수
# 정렬을 목적으로 하는 함수를 값으로 넣어줌 >> x:x[0] (x[0]이 정렬기준) 
# 즉 21, 20과 같이 나이를 기준으로 정렬하기 떄문에 입력순서로 남을 수 있다.
for i in range(n):
    print("{} {}".format(li[i][0], li[i][1]))