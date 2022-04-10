# coding=utf-8
#######################################################################################################################
#  Name:          Burak Karataş
#  Student ID:    64200045
#  Department:    Computer Engineering
#
#  Assignment ID: A2
#######################################################################################################################
########################################################################################################################
#
#Question I:
#Write a program that prompts the user to enter a grade between 0 and 100 and displays its corresponding letter grade
#according to the following table. Here are some sample runs:
#Enter a grade value (0 to 100): 75
#
#The letter grade is B-
#Enter a grade value (0 to 100): 59

#The letter grade is F
#Enter a grade value (0 to 100): 96
#The letter grade is A
#GRADE LETTER GRADE
#95-100 A
#
#90-94 A-
#85-89 B+
#
#80-84 B
#
#75-79 B-
#70-74 C+
#
#65-69 C
#
#60-64 C-
#0-59 F
#
########################################################################################################################
print("\n")
print("Solution of Question 1")
print("\n")

degree = int(input("Enter your grade :"))

if degree >= 95:
    print(" Your grade is: A ")
elif degree >= 90:
    print(" Your grade is: A - ")
elif degree >= 85:
    print(" Your grade is: B + ")
elif degree >= 80:
    print(" Your grade is: B ")
elif degree >= 75:
    print(" Your grade is: B - ")
elif degree >= 70:
    print(" Your grade is: C+ ")
elif degree >= 65:
    print(" Your grade is: C ")
elif degree >= 60:
    print(" Your grade is: C - ")
else:
    print(" Your grade is: F ")

########################################################################################################################
#
#Question II:
#(Geometry: point in a rectangle?) Write a program that prompts the user to enter a point (x, y) and checks whether
#the point is within the rectangle centered at (0, 0) with width 10 and height 5. For example, (2, 2) is inside the
#rectangle and (6, 4) is outside the rectangle, as shown in the following Figure. (Hint: A point is in the rectangle if its
#horizontal distance to (0, 0) is less than or equal to 10 / 2 and its vertical distance to (0, 0) is less than or equal to 5.0 /
#2. Test your program to cover all cases.)
#
########################################################################################################################
print("\n")
print("Solution of Question 2")
print("\n")

x = int(input("Enter coordinate X: "))
y = int(input("Enter coordinate Y: "))

if 11 > x > -11 and 6 > y > -6:
    print("Your point is in the rectangle.")
else:
    print("Your point is not in the rectangle.")

################################################################################################################################
#
#Question III:
#Write a program that prints the following patterns separately, one below the other each pattern separated from the next by one
#blank line. Use for loops to generate the patterns.
#
##################################################################################################################################

print("\n")
print("Solution of Question 3")
print("\n")

rows = 10

for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

print("\n")
print("==========================")
print("\n")

rows = 10
for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")

print("\n")
print("==========================")
print("\n")

rows = 10
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if(j < i):
            print(' ', end = '  ')
        else:
            print('*', end = '  ')
    print()

print("\n")
print("==========================")
print("\n")

rows = 10
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        print("* ", end="")
    print("")

print("\n")
print("==========================")
print("\n")

################################################################################################################################
#Question IV:
#Write a program that computes π using the following series expansion.
#
#Write a program that displays the π value for i = 100, 500, 1000 and 10000. Your program should also display the
#difference between the approximate π value that you calculated with the series formula and the π value using math
#library (use math.pi).
#You can use a nested loop like:
# Take each value of i.
#for i in [100,500,1000, 10000]:
# compute pi number
#for j in range(1,i):
#
################################################################################################################################

print("\n")
print("Solution of Question 4")
print("\n")

def Leibniz(i):

    a = 1
    b = 1

    for i in range(i):
        a = a + 2
        b = b - (1/a)
        a = a + 2
        b = b + (1/a)

    Result = b * 4

    return (Result)

print(Leibniz(100))
print(Leibniz(500))
print(Leibniz(1000))
print(Leibniz(10000))

################################################################################################################################
#Question V:
#Using Turtle graphics, plot the sine and cosine function. The program plots the sine function in red and cosine in
#blue, as shown in Figure b.
#
################################################################################################################################

print("\n")
print("Solution of Question 5")
print("\n")

import turtle
import math

turtle.speed(3)

turtle.penup()
turtle.goto(-220, 0)
turtle.pendown()
turtle.goto(220, 0)

turtle.setheading(150)
turtle.forward(20)
turtle.penup()
turtle.goto(220, 0)
turtle.setheading(-150)
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(0, 110)
turtle.write('Y')

turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.goto(0, 100)

turtle.setheading(240)
turtle.forward(20)
turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.setheading(-60)
turtle.forward(20)

turtle.penup()
turtle.goto(225, 0)
turtle.write('X')

x = -175
turtle.pensize(2)
turtle.color('blue')
turtle.penup()
turtle.goto(x, 50 * math.sin((x / 100) * 2 * math.pi))
turtle.pendown()
for x in range(-175, 176):
    turtle.goto(x, 50 * math.sin((x / 100) * 2 * math.pi))

turtle.penup()
turtle.goto(-100, -20)
turtle.write('-2π')

turtle.penup()
turtle.goto(100, -20)
turtle.write('2π')

x = -175
turtle.pensize(2)
turtle.color('red')
turtle.penup()
turtle.goto(x, 50 * math.cos((x / 100) * 2 * math.pi))
turtle.pendown()
for x in range(-175, 176):
    turtle.goto(x, 50 * math.cos((x / 100) * 2 * math.pi))

turtle.hideturtle()
turtle.done()



