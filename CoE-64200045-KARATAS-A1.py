# coding=utf-8
#######################################################################################################################
#  Name:          Burak Karataş
#  Student ID:    64200045
#  Department:    Computer Engineering
#
#  Assignment ID: A1
#######################################################################################################################

#######################################################################################################################
#QUESTION I
# Description:
# Write a program that displays the following table:--
#
# a a^2 a^3 a^4
# 1 1 1 1
# 2 4 8 16
# 3 9 27 81
# 4 16 64 256
#
#
#########################################################################################

print("\n")
print("SOLUTION OF QUESTION 1")
print('========================')
print('a', 'a^2', 'a^3', 'a^4')
k = 2 * 1, 2 * 2, 2 * 3, 2 * 4
l = 3 * 1, 3 * 2, 3 * 3, 3 * 4
m = 4 * 1, 4 * 2, 4 * 3, 4 * 4
print(k)
print(l)
print(m)


# Another option for calculating results of exponential numbers.

print("\n")
print("ALTERNATE SOLUTION OF QUESTION 1")
print('========================')

base = input("Enter your base: ")
exponent = input("Enter your exponent: ")
print("Exponential Value is: "), pow(base, exponent)


#QUESTION II
# Description:
#
#  An approximate value of pi number can be computed using the following formula.
#
#
#########################################################################################

print("\n")
print("SOLUTION OF QUESTION 2")
print('========================')

k = float(1)
a = float(4)
b = float(1/3)
c = float(1/5)
d = float(1/7)
e = float(1/9)
f = float(1/11)
g = float(1/13)
j = float(1/15)


pi1 = float(a * (k-b+c-d+e-f))
pi2 = float(a * (k-b+c-d+e-f+g-j))
print (float(pi1))
print (float(pi2))



#QUESTION III
# Description:
#
# Write a program that prompts the user to enter a six digit integer and displays the number in reverse order. (Don’t
# use indexing. You can use arithmetic operation.) Here is a sample run:
#
# Enter an integer:673248
#
# 6
# 7
# 3
# 2
# 4
# 8
#
#########################################################################################

print("\n")
print("SOLUTION OF QUESTION 3")
print('========================')

number = 456219
a = 456219 % 10
b = 45621 % 10
c = 4562 % 10
d = 456 % 10
e = 45 % 10
f = 4 % 10

print(number)
print("\n")
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


#QUESTION IV
# Description:
#
# Write a program that receives a character and displays its UNICODE code. For example, if the user enters Ş, the
# program displays the character 351. Here is a sample run:
#
# Enter a character : Ş
# The UNICODE of character Ş is 351
#
#
#
#########################################################################################

print("\n")
print("SOLUTION OF QUESTION 4")
print('========================')


## Enter Your Character like "A". You have to use double quotes.

Character = input("Enter your character: ")
value = ord(Character)
print ("UNICODE of character is: "), value


#QUESTION V
# Description:
#
# Write a program that generates figures A and B by using the turtle graphics library.
#
#
#########################################################################################


print("\n")
print("SOLUTION OF QUESTION 5.1")
print('========================')

import turtle



# Draw External Square for Triangle


# Black Borderline

turtle.pensize(2)
turtle.pencolor("black")
turtle.fillcolor("black")
turtle.penup()
turtle.goto(-550, -150)
turtle.pendown()
turtle.forward(500)
turtle.left(90)
turtle.forward(500)
turtle.left(90)
turtle.forward(500)
turtle.left(90)
turtle.forward(500)
turtle.left(90)
turtle.circle(40, steps=1)
turtle.hideturtle()

turtle.pensize(3)
turtle.color("black")
turtle.penup()
turtle.goto(-310, -180)
turtle.write("Figure A")


turtle.pensize(3)
turtle.pencolor("red")

turtle.penup()
turtle.goto(-510, -85)
turtle.pendown()
turtle.forward(170)
turtle.left(90)
turtle.forward(170)
turtle.left(90)
turtle.forward(170)
turtle.left(90)
turtle.forward(170)
turtle.left(90)
turtle.circle(40, steps=1)
turtle.hideturtle()

# Draw Triangle

turtle.pensize(3)
turtle.pencolor("red")
turtle.fillcolor("red")
turtle.begin_fill()
turtle.penup()
turtle.goto(-475, -45)
turtle.pendown()
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.circle(40, steps = 1)
turtle.end_fill()
turtle.hideturtle()

turtle.pensize(3)
turtle.color("black")
turtle.penup()
turtle.goto(-440, -65)
turtle.write("Triangle")


# Draw External Square for Square

turtle.pensize(3)
turtle.pencolor("blue")
turtle.fillcolor("blue")
turtle.penup()
turtle.goto(-510, 135)
turtle.pendown()
turtle.forward(170)
turtle.left(90)
turtle.forward(170)
turtle.left(90)
turtle.forward(170)
turtle.left(90)
turtle.forward(170)
turtle.left(90)
turtle.circle(40, steps=1)
turtle.hideturtle()



# Draw Square

turtle.pensize(3)
turtle.pencolor("blue")
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.penup()
turtle.goto(-475, 170)
turtle.pendown()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.circle(40, steps=1)
turtle.end_fill()
turtle.hideturtle()

turtle.pensize(3)
turtle.color("black")
turtle.penup()
turtle.goto(-440, 150)
turtle.write("Square")


# Draw External Square for Circle


turtle.pensize(3)
turtle.pencolor("green")
turtle.fillcolor("green")
turtle.penup()
turtle.goto(-285, 130)
turtle.pendown()
turtle.forward(170)
turtle.left(90)
turtle.forward(170)
turtle.left(90)
turtle.forward(170)
turtle.left(90)
turtle.forward(170)
turtle.left(90)
turtle.circle(40, steps=1)
turtle.hideturtle()

# Draw Circle

turtle.pensize(3)
turtle.pencolor("green")
turtle.fillcolor("green")
turtle.begin_fill()
turtle.penup()
turtle.goto(-200, 170)
turtle.pendown()
turtle.forward(0)
turtle.left(360)
turtle.circle(40)
turtle.end_fill()
turtle.hideturtle()

turtle.pensize(3)
turtle.color("black")
turtle.penup()
turtle.goto(-210, 140)
turtle.write("Circle")


# Draw External Square for Rectangle

turtle.pensize(3)
turtle.pencolor("yellow")
turtle.fillcolor("yellow")
turtle.penup()
turtle.goto(-285, -87)
turtle.pendown()
turtle.forward(170)
turtle.left(90)
turtle.forward(170)
turtle.left(90)
turtle.forward(170)
turtle.left(90)
turtle.forward(170)
turtle.left(90)
turtle.circle(40, steps=1)
turtle.hideturtle()

# Draw Rectangle

turtle.pensize(3)
turtle.pencolor("yellow")
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.penup()
turtle.goto(-275, -47)
turtle.pendown()
turtle.forward(150)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.circle(40, steps=1)
turtle.end_fill()
turtle.hideturtle()


turtle.pensize(3)
turtle.color("black")
turtle.penup()
turtle.goto(-215, -75)
turtle.write("Rectangle")



print("\n")
print("SOLUTION OF QUESTION 5.2")
print('========================')

import turtle

turtle.pensize(3)
turtle.pencolor("black")

turtle.begin_fill()
turtle.penup()
turtle.goto(200, -50)
turtle.pendown()

# Square

turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.circle(40, steps=1)
turtle.hideturtle()


turtle.pensize(3)
turtle.color("black")
turtle.penup()
turtle.goto(260, -70)
turtle.write("Figure B")

# Circle

turtle.pensize(3)
turtle.pencolor("blue")
turtle.penup()
turtle.goto(275, -47)
turtle.pendown()
turtle.forward(0)
turtle.left(360)
turtle.circle(72)
turtle.hideturtle()




# Blue Straight Line

turtle.pensize(3)
turtle.pencolor("blue")
turtle.penup()
turtle.goto(200, 25)
turtle.pendown()
turtle.forward(150)


# Red Shapes

turtle.pensize(3)
turtle.pencolor("red")
turtle.penup()
turtle.goto(210, -50)
turtle.pendown()
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(10)

turtle.pensize(3)
turtle.pencolor("red")
turtle.penup()
turtle.goto(210, 100)
turtle.pendown()
turtle.left(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(10)

turtle.pensize(3)
turtle.pencolor("red")
turtle.penup()
turtle.goto(340, 100)
turtle.pendown()
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(10)
turtle.pensize(3)
turtle.pencolor("red")
turtle.penup()
turtle.goto(340, -50)
turtle.pendown()
turtle.left(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(10)


#Dashed Black Lines

turtle.color("black")
turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.left(45)
turtle.forward(10)
turtle.penup()
turtle.forward(5)
turtle.pendown()
turtle.forward(10)
turtle.penup()
turtle.forward(5)
turtle.pendown()
turtle.forward(10)
turtle.penup()
turtle.forward(5)
turtle.pendown()
turtle.forward(10)
turtle.penup()
turtle.forward(5)
turtle.pendown()
turtle.forward(10)
turtle.penup()
turtle.forward(5)
turtle.pendown()
turtle.forward(10)
turtle.penup()
turtle.forward(5)
turtle.pendown()
turtle.forward(10)
turtle.penup()
turtle.forward(5)
turtle.pendown()
turtle.forward(10)
turtle.penup()
turtle.forward(5)
turtle.pendown()
turtle.forward(10)
turtle.penup()
turtle.forward(5)
turtle.pendown()
turtle.forward(10)
turtle.penup()
turtle.forward(5)
turtle.pendown()
turtle.forward(10)
turtle.penup()
turtle.forward(5)
turtle.pendown()
turtle.forward(10)
turtle.penup()
turtle.forward(5)
turtle.pendown()
turtle.forward(10)
turtle.penup()
turtle.forward(5)
turtle.pendown()
turtle.forward(15)


turtle.exitonclick()
