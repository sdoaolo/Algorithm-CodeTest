#1110_더하기 사이클
n = input()
if len(n)==1:
		n = "0"+n	
i = 0
new = n
if n != "00":
	while True:	
		i += 1
		sum = str(int(new[0])+int(new[1]))
		if len(sum)== 1:
			sum = "0" + sum
			
		new = new[1] +sum[1]	
	
		if (new == n):
			print(i)
			break
else:
	print(1)
