#6588

MAX = 1000000
check = [0] * (MAX+1)
check[0] = check[1] = True

prime = [] #prime set

for i in range(2,int(MAX**0.5)+1):
	if not check[i]:
		prime.append(i)
		j = i+i
		while(j<MAX):
			check[j] = True
			j +=i

prime = prime[1:] # 2를 빼줌 >> a와 b는 홀수 소수이기 때문에 

while 1:
	n = int(input())
	if n == 0: 
		break
	for p in prime:
		if check[n-p] == False:
			print(n ,"=" ,p , "+", n-p)
			break