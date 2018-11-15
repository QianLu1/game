from Tkinter import *

master = Tk()

w = Canvas(master, width=1000, height=600)
w.pack()

w.create_line(1*30,30,1*30,480,width=2)
w.create_line(2*30,30,2*30,480,width=2)
for num in range(0, 17):
    w.create_line(num*30, 30, num*30, 480, width=2)
for num in range(0, 17):
    w.create_line(30, num*30, 480, num*30, width=2)
# w.create_line(0, 100, 200, 0, fill="red")

# w.create_rectangle(50, 25, 150, 75, fill="blue")

mainloop()
def paint(event):
    python_green = 'blue'
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    w.create_oval(x1, y1, x2, y2, fill = python_green)
master = Tk()
master.time('Paint')
w = Canvas(master, width = 10, height=10)
w.pack(expand = YES, fill = BOTH)
w.bind("<Button-1>", paint)
message = Label(master, text = "Press and Drag the mouse to draw")
message.pack(side = BOTTOM)

