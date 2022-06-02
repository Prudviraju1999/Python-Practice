n = input()
length = len(n)
x,s = 9,0
for i in range(1,length):
 s=s+x*i
 x = x*10
print(s+(int(n)-10**(length-1)+1)*length)
