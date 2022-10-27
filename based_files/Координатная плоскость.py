from tkinter import *
a = Tk()

x = int(input('длина окна:'))
y = int(input('высота окна:'))
m = int(input('цена деления:'))

b = Canvas(a, width=x, height=y)
b.pack()
def os(x, y, m):
    b.create_line(x//2, 0, x//2, y, width=2)
    b.create_line(0, y//2, x, y//2, width=2)
    for k in range(0, x, m):
        b.create_line(k, y//2-10, k, y//2+10)
    for k in range(0, y, m):
        b.create_line(x//2-10, k, x//2+10, k)

os(x, y, m)
a.mainloop()