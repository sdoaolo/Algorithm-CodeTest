#2754_학점계산

sc = input()
l = {"A":4,"B":3,"C":2,"D":1,"F":0}
res = float(l[sc[0]])

if sc != "F":
	if sc[1] == '+':
		res += 0.3
	elif sc[1] == '-':
		res -= 0.3
	
print(res)