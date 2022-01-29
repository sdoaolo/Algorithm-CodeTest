#17614 369

n = int(input())

clap = 0 

for i in range(1,n+1):
   clap += str(i).count('3')
   clap += str(i).count('6')
   clap += str(i).count('9')
   
print(clap)