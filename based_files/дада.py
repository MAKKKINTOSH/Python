a = 4**2016 - 2**2018+8**800-80
count=0
while a>=2:
    if a%2 == 1:
        count+=1
    a=a//2
if a%2 ==1:
    count+=1
print(count)