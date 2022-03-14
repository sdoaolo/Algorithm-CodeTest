# 2941_크로아티아 알파벳

cr = ["c=","c-","dz=","d-","lj","nj","s=","z="]

m = input()

for c in cr:
    m = m.replace(c,"0")

print(len(m))