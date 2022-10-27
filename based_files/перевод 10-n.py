n = 6
a = 15
m=str()
while a>=n:
    m = str(a%n)+m
    a=a//n
m = str(a%n)+m
print(m)