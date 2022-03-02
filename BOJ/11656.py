#11656_접미사 배열

s = input()
l = len(s)
li = []

for i in range(l, 0 ,-1):
    li.append(s[l-i:])
    
li.sort()
for i in li:
    print(i)

    