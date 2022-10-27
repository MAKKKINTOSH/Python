from tkinter import *
from math import sqrt

a = Tk()
xm = 1920
ym = 1080
dm = 50
b = Canvas(a, width=xm, height=xm)
b.pack()

x = int(input('Длина комнаты:'))
y = int(input('Ширина комнаты:'))
z = int(input('Высота потолков:'))

x_rt = xm//2 + x*dm//2
y_up = ym//2 - y*dm//2
y_dn = ym//2 + y*dm//2
x_lt = xm//2 - x*dm//2

b.create_line(x_rt, y_up, x_rt, y_dn)
b.create_line(x_rt, y_dn, x_lt, y_dn)
b.create_line(x_lt, y_dn, x_lt, y_up)
b.create_line(x_lt, y_up, x_rt, y_up)

pl = int(input('расстояние до динамика от верхней или левой крайней точки стены:'))
b.create_oval((xm // 2 + x * dm // 2)-5, (ym // 2 - y * dm // 2 + y * dm) - pl*dm - 5, (xm // 2 + x * dm // 2) + 5, (ym // 2 - y * dm // 2 + y * dm) - pl*dm + 5, fill = 'green')
print(pl*dm, (ym // 2 - y * dm // 2 + y * dm) - pl*dm, y//2*dm)
a.mainloop()