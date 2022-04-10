from tkinter import *

class Main():

    def left(self,event):
        self.canvas.move(self.oval, -10, 0)
    def right(self,event):
        self.canvas.move(self.oval, 10, 0)
    def up(self,event):
        self.canvas.move(self.oval, 0, -10)
    def down(self,event):
        self.canvas.move(self.oval, 0, 10)

    def __init__(self):
        window = Tk()
        window.title("Move the Circle")

        self.canvas = Canvas(window, bg="white", width=300, height=300)
        self.canvas.pack()
        self.canvas.create_oval(20, 20, 80, 80, tags="ball1", fill="blue")
        self.canvas.create_oval(100, 20, 160, 80, tags="ball3", fill="black")
        self.canvas.create_oval(60, 50, 120, 110, tags="ball2", fill="yellow")
        self.canvas.create_oval(180, 20, 240, 80, tags="ball5", fill="red")
        self.oval = self.canvas.create_oval(140, 50, 200, 110, tags="ball4", fill="green")
        self.canvas.focus_set()

        frame = Frame(window)
        frame.pack()

        self.canvas.bind("<Up>", self.up)
        self.canvas.bind("<Down>", self.down)
        self.canvas.bind("<Right>", self.right)
        self.canvas.bind("<Left>", self.left)
        self.canvas.bind("<B1-Motion>", self.Color)
        window.mainloop()

    def Color(self, event):
        if colorBall2(event.x, event.y):
            self.canvas.itemconfig("ball2", fill="hotpink")
            self.canvas.itemconfig("ball1", fill="blue")
            self.canvas.itemconfig("ball3", fill="black")
            self.canvas.itemconfig("ball4", fill="green")
            self.canvas.itemconfig("ball5", fill="red")
        elif colorBall4(event.x, event.y):
            self.canvas.itemconfig("ball4", fill="hotpink")
            self.canvas.itemconfig("ball1", fill="blue")
            self.canvas.itemconfig("ball3", fill="black")
            self.canvas.itemconfig("ball2", fill="yellow")
            self.canvas.itemconfig("ball5", fill="red")
        elif colorBall3(event.x, event.y):
            self.canvas.itemconfig("ball1", fill="blue")
            self.canvas.itemconfig("ball3", fill="hotpink")
            self.canvas.itemconfig("ball4", fill="green")
            self.canvas.itemconfig("ball5", fill="red")
            self.canvas.itemconfig("ball2", fill="yellow")
        elif colorBall5(event.x, event.y):
            self.canvas.itemconfig("ball5", fill="hotpink")
            self.canvas.itemconfig("ball1", fill="blue")
            self.canvas.itemconfig("ball3", fill="black")
            self.canvas.itemconfig("ball4", fill="green")
            self.canvas.itemconfig("ball2", fill="yellow")
        elif colorBall1(event.x, event.y):
            self.canvas.itemconfig("ball1", fill="hotpink")
            self.canvas.itemconfig("ball2", fill="yellow")
            self.canvas.itemconfig("ball3", fill="black")
            self.canvas.itemconfig("ball4", fill="green")
            self.canvas.itemconfig("ball5", fill="red")
        else:
            self.canvas.itemconfig("ball1", fill="blue")
            self.canvas.itemconfig("ball2", fill="yellow")
            self.canvas.itemconfig("ball3", fill="black")
            self.canvas.itemconfig("ball4", fill="green")
            self.canvas.itemconfig("ball5", fill="red")



def colorBall1(x, y):
    if abs(50 - x) < 30 and abs(50 - y) < 30:
        return True
def colorBall2(x, y):
    if abs(90 - x) < 30 and abs(80 - y) < 30:
        return True
def colorBall4(x, y):
    if abs(170 - x) < 30 and abs(80 - y) < 30:
        return True
def colorBall3(x, y):
    if abs(130 - x) < 30 and abs(50 - y) < 30:
        return True
def colorBall5(x, y):
    if abs(210 - x) < 30 and abs(50 - y) < 30:
        return True




Main()