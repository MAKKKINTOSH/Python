from tkinter import *
from math import *
a = Tk()
xm = 1920
ym = 1080
dm = 50
b = Canvas(a, width = xm, height = xm)
b.pack()

x = float(input('Длина комнаты:'))
y = float(input('Ширина комнаты:'))
z = float(input('Высота потолков:'))
w = float(input('Высота расчетной точки:'))

x_rt = xm//2 + x*dm//2
y_up = ym//2 - y*dm//2
y_dn = ym//2 + y*dm//2
x_lt = xm//2 - x*dm//2

b.create_line(x_rt, y_up, x_rt, y_dn)
b.create_line(x_rt, y_dn, x_lt, y_dn)
b.create_line(x_lt, y_dn, x_lt, y_up)
b.create_line(x_lt, y_up, x_rt, y_up)

pl = int(input('расстояние до динамика от нижней точки стены:'))
db = int(input('Звуковое давление динамика:'))
b.create_oval(x_rt - 5, y_dn - pl * dm - 5, x_rt + 5, y_dn - pl * dm + 5, fill='green')

if y - pl >= y//2:
    y2 = y_up
    ay = y - pl
elif y - pl < y//2:
    y2 = y_dn
    ay = pl
b.create_line(x_rt, y_dn - pl * dm, x_lt, y2)
dist = sqrt(x**2+ay**2+(z-w)**2)
dbmin = 20 * log10(dist)
decb = db - floor(dbmin)

print('Расстояние от динамика до дальней точки:', dist)
print('Звуковое давление в дальней точке:', decb)
a.mainloop()