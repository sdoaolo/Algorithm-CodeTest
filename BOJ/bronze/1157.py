# 1157

s = input().upper()

max = -1
maxChar = ""
sett = set()
cnt = []

for i in s:
    if i not in sett:
        sett.add(i)
        c = s.count(i)
        if c >= max:
            max = c
            maxChar = i
            cnt.append(c)

for i in range(len(cnt)):
    cc = cnt.count(cnt[i])
    if cc > 1 and cnt[i] == max:
        maxChar = "?" 
    
print(maxChar)