from tkinter import *
import math

class RegularPolygonCanvas(Canvas):
    def __init__(self, parent, numberOfSides=4, width=150, height=150):
        super().__init__(parent, width=width, height=height)
        self.setNumberOfSides(numberOfSides)

    def getNumberOfSides(self):
        return self.numberOfSides

    def setNumberOfSides(self, numberOfSides):
        self.numberOfSides = numberOfSides
        self.drawPolygon()

    def Increase(self):
        self.setNumberOfSides(int(self.getNumberOfSides()) + 1)
        self.drawPolygon()

    def Decrease(self):
        self.setNumberOfSides(int(self.getNumberOfSides()) - 1)
        self.drawPolygon()

    def drawPolygon(self):
        self.delete("polygon")
        width = int(self["width"])
        height = int(self["height"])
        xCenter = width / 2
        yCenter = height / 2;
        radius = min(width, height) * 0.4
        angle = 2 * math.pi / self.numberOfSides
        polygon = []
        for i in range(self.numberOfSides):
            polygon.append([xCenter + radius * math.cos(i * angle),
                            yCenter - radius * math.sin(i * angle)])
        self.create_polygon(polygon, fill="red", tags="polygon")

class MainClass:
    def __init__(self):
        window = Tk()
        window.title("Regular Polygons")
        canvas = RegularPolygonCanvas(window, 3)
        canvas.pack(side=LEFT)
        but1 = Button(window, text="Increase", command= canvas.Increase).pack(side=BOTTOM)
        but2 = Button(window, text="Decrease", command= canvas.Decrease).pack(side=BOTTOM)
        window.mainloop()

MainClass()