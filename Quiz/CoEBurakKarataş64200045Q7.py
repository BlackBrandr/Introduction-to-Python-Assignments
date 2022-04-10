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

        self.canvas = Canvas(window, bg ="white", width = 600, height = 600)
        self.canvas.pack()
        self.oval = self.canvas.create_oval(100, 100, 40, 40, fill="white")
        self.canvas.focus_set()

        frame = Frame(window)
        frame.pack()

        self.canvas.bind("<Up>", self.up)
        self.canvas.bind("<Down>", self.down)
        self.canvas.bind("<Right>", self.right)
        self.canvas.bind("<Left>", self.left)
        window.mainloop()

Main()