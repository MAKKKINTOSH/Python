n = 7
a = 120
m=0
for k in range(len(str(a))):
    m += (a%10)*n**k
    a=a//10
print(m)