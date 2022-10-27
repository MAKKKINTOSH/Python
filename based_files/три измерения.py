from tkinter import *
from math import *
a = Tk()

x = 1920
y = 1080

b = Canvas(a, width=x, height=y)
b.pack()
def os(x, y):
    b.create_line(x//2, 0, x//2, y, width=1)
    b.create_line(0, y//2, x, y//2, width=1)
os(x, y)
a.mainloop()