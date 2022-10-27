from tkinter import *
a = Tk()

b = Canvas(a, width=1000, height=800)
b.pack()
b.create_line(500, 0, 500, 800, width=3)
b.create_line(0, 400, 1000, 400, width=3)
for k in range(0, 1000, 50):
    b.create_line(k, 375, k, 425)
for k in range(0, 800, 50):
    b.create_line(475, k, 525, k)
a.mainloop()