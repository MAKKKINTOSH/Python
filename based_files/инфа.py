a=int(input())
b=int(input())
c = 0
s = []
a1 = hex(a)[2:]
b1 = hex(b)[2:]
for x in a:
    for y in b:
        s += [x + y]
        if x < 6 or y < 6:
            c = 1
if len(a1) == 2 and len(b1) == 2 and c == 0:
print(s)