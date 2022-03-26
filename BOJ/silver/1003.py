#1003_피보나치 함수_dp_silver3_다시풀어보기~!
import sys
input = sys.stdin.readline

#각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.

#fibo(0) 은 0 > 1번 호출, 1 > 0번 호출이므로 각 zero, one 리스트 0번째 인덱스에 1, 0으로 초기화
# 마찬가지로 fibo(1)은 0> 0번 1>1번 호출이므로 초기화
#fibo(2) > 1, 0 한번씩 호출

zero = [1, 0, 1]
one = [0, 1, 1]

#0 ~ 40까지 구하면 되므로 3부터 41
# fibo 3은 2(1,0)와 1호출 이므로  0> 1번, 1> 2번 
#지금까지 관계를 보면, 다음과 같은 식을 만들수 있다. 
for i in range(3, 41):
    zero.append(zero[i-1]+zero[i-2])
    one.append(one[i-1]+one[i-2])

t = int(input())

for i in range(t):
    n = int(input())
    print(f'{zero[n]} {one[n]}') 
