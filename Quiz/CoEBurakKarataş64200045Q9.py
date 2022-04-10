# QUESTION 1


from tkinter import *  # Import tkinter
import math

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def isInside(self, x, y):
        return distance(self.x, self.y, x, y) <= self.radius

width = 400
height = 250
x = 100
y = 100
hGap = 120
vGap = 50
radius = 50


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Dragging The Blue Circle")  # Set title

        self.canvas = Canvas(window, width=width, height=height)
        self.canvas.pack()

        self.c1 = Circle(x, y, radius)
        self.c2 = Circle(x + hGap, y, radius)
        self.c3 = Circle(x + 2 * hGap, y, radius)
        self.c4 = Circle(x + radius, y + vGap, radius)
        self.c5 = Circle(x + 190, y + vGap, radius)

        self.paint(self.c1, "blue", "c1")
        self.paint(self.c2, "black", "c2")
        self.paint(self.c3, "red", "c3")
        self.paint(self.c4, "yellow", "c4")
        self.paint(self.c5, "green", "c5")

        self.canvas.bind("<B1-Motion>", self.mouseMoved)


        window.mainloop()

    def mouseMoved(self, event):
        if self.c1.isInside(event.x, event.y):
            self.c1.x = event.x
            self.c1.y = event.y
            self.canvas.delete("c1")
            self.paint(self.c1, "blue", "c1")


        elif self.c2.isInside(event.x, event.y):
            self.c2.x = event.x
            self.c2.y = event.y
            self.canvas.delete("c2")
            self.paint(self.c2, "black", "c2")

        elif self.c3.isInside(event.x, event.y):
            self.c3.x = event.x
            self.c3.y = event.y
            self.canvas.delete("c3")
            self.paint(self.c3, "red", "c3")

        elif self.c4.isInside(event.x, event.y):
            self.c4.x = event.x
            self.c4.y = event.y
            self.canvas.delete("c4")
            self.paint(self.c4, "yellow", "c4")

        elif self.c5.isInside(event.x, event.y):
            self.c5.x = event.x
            self.c5.y = event.y
            self.canvas.delete("c5")
            self.paint(self.c5, "green", "c5")

    def paint(self, c, color, tags="stable"):
        self.canvas.create_oval(c.x - c.radius, c.y - c.radius, c.x + c.radius, c.y + c.radius, fill=color,
                                activefill="gold", tags=tags)

def distance(x1, y1, x2, y2):
    return ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5

MainGUI()


# QUESTION 2

import math

def summ(PARAMETERS):
    SUM = 0
    print("Parametreler:",PARAMETERS)
    for i in PARAMETERS:
        SUM += i
    return SUM

numbers = [int(x) for x in input("Enter values: ").split(" ")]

print("Sum of numbers: ", summ(numbers))

def MEAN(numbers):

    a = sum(numbers) / len(numbers)
    print("Mean:",a)
    return a

def standartsapma(numbers):
    sum_of_squares = 0
    for i in numbers:
        sum_of_squares += i**2
    total = 0
    for j in numbers:
        total += j
    square_of_sum = total ** 2
    return print("Standard Deviation: ", math.sqrt((sum_of_squares-square_of_sum/len(numbers))/(len(numbers)-1)))

MEAN(numbers)
standartsapma(numbers)