from tkinter import *
a = Tk()

x = int(input('длина окна:'))
y = int(input('высота окна:'))
m = int(input('цена деления:'))

b = Canvas(a, width=x, height=y)
b.pack()
def os(x, y, m):
    b.create_line(x//2, 0, x//2, y, width=1)
    b.create_line(0, y//2, x, y//2, width=1)
    for k in range(0, x, m):
        b.create_line(k, y//2-5, k, y//2+5)
    for k in range(0, y, m):
        b.create_line(x//2-5, k, x//2+5, k)

os(x, y, m)

x1 = -(x//(m*2))
y1 = x1 ** 2
for x2 in range(x1 + 1, x//(m*2) + 1):
    y2 = x2 ** 2
    b.create_line(x1*m+x//2, -y1*m+y//2, x2*m+x//2, -y2*m+y//2)
    x1 = x2
    y1 = y2
a.mainloop()