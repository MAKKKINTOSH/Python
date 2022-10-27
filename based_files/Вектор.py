from tkinter import *
from random import randint
from math import hypot
a = Tk()

b = Canvas(a, width = 1000, height = 1000)
b.pack()
x1 = randint(100, 900)
y1 = randint(100, 900)
x2 = randint(100, 900)
y2 = randint(100, 900)
b.create_line(x1, y1, x2, y2, width = 2)



print(x1, y1, x2, y2)
print(hypot(max(x1,x2)-min(x1,x2), max(y1,y2)-min(y1,y2)))
a.mainloop()