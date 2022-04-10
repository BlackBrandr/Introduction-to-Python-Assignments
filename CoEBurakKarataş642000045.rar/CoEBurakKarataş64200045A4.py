#########################################################################################
# Name: Burak Karataş
# Student ID: 64200045
# Department: Computer Engineering
#
# Assignment ID: A4
########################################################################################


########################################################################################
# Question I:
# Generate a list of 300 random values in the range 1–99. Determine, print, and remove duplicate values
# of numbers from the list that appears more than 2 times. Your program should print
# - sorted original list generated randomly, (Ex: [1,1,4,4,4,5,6,6,10,10,10,10])
# - duplicate values that appear more than 2 times, and (Ex : [4,4,4,10,10,10,10])
# - the list without duplicates that appear more than 2 times. (Ex: [1,1,5,6,6])
# (Hint: you many want to sort the list first.)
########################################################################################

print("\n")
print("********************************************************************************")
print("SOLUTION OF QUESTION I:")
print("********************************************************************************"),
print("\n")

import random
import collections

def mainn():
    List1 = []
    for i in range(300):
      List1.append(random.randint(1,99))

    SORT = sorted(List1)
    print(SORT)

    ctlist = collections.Counter(SORT)

    print("count is more than 2",[item for item in SORT if ctlist[item] > 2])
    print("count is less than equal to 2",[item for item in SORT if ctlist[item] <= 2])

mainn()

########################################################################################
# Question II:
# Write the missing functions myAverage, myStandardDev, myMin, and myCorrelation in the following
# code. The formulas for average (mean), standard deviation and correlation are given below.
########################################################################################

print("\n")
print("********************************************************************************")
print("SOLUTION OF QUESTION II:")
print("********************************************************************************"),
print("\n")


import numpy as np
import math

def myAvearage(lst):

    a = sum(lst) / len(lst)
    return a

def myStandardDev(lst):

    sum_of_squares = 0
    for i in lst:
        sum_of_squares += i ** 2
    total = 0
    for j in lst:
        total += j
    square_of_sum = total ** 2
    return (math.sqrt((sum_of_squares - square_of_sum / len(lst)) / (len(lst) - 1)))

def myMin(lst):

    lst.sort()
    x = (lst[:1])
    return x

def myCorrelation(x,y):

    c = np.corrcoef(x,y)

    return c

def main():

    aList = [11, 20, 30, 50, 80, 90, 101, 15, 125, 128, 150, 185, 200, 240, 260, 290]
    bList = [14, 25, 28, 45, 79, 85, 121, 115, 125, 256, 160, 195, 230, 270, 280, 330]
    cList = bList.copy()
    cList.reverse()
    dList = [random.randint(1,99) for x in range(len(aList))]

    print("Lists:")
    print("List A = " + str(aList))
    print("List B = " + str(bList))
    print("List C = " + str(cList))
    print("List D = " + str(dList))

    print()
    print("List A Average = " + str(myAvearage(aList)))
    print("Standart Deviation of List A = ", str(myStandardDev(aList)))
    print("Minimum of List A = " + str(myMin(aList)))

    print()
    print("List B Average = " + str(myAvearage(bList)))
    print("Standart Deviation of List B = ", str(myStandardDev(bList)))
    print("Minimum of List B = " + str(myMin(bList)))

    print()
    print("Correlation of List A and B = ", str(myCorrelation(aList, bList)))
    print("Correlation of List A and C = ", str(myCorrelation(aList, cList)))
    print("Correlation of List A and D = ", str(myCorrelation(aList, dList)))

main()


########################################################################################
# Question III:
# In this question, you are going to write methods that operate on matrices. The program reads values of
# matrices A, B, and C stored in a file called inputs.txt. This file should be placed under current directory
# where you have the program. The first line before each matrix contains the number of rows and the
# number of columns as shown below.
# <Input>
# 4 4
# 55 55 55 56
# 66 20 12 67
# 77 15 25 78
# 88 12 13 89
# 4 4
# 1 2 3 4
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4
# 4 4
# 50 12 75 14
# 55 24 24 25
# 33 34 35 36
# 44 45 46 47
# <End Input>
# As a first step, the program reads data for matrices A, B and C from inputs.txt file and write them into
# console. A fourth matrix D is generated randomly and printed. A partial program code is given below.
########################################################################################


print("\n")
print("********************************************************************************")
print("SOLUTION OF QUESTION III:")
print("********************************************************************************"),
print("\n")

import random
import sys

def readMatrix(numberOfRows, numberOfColumns, file):
    matrix = []

    for row in range(numberOfRows):

        matrix.append([])

        line = file.readline()

        rowdata = [int(x) for x in line.split(' ')]

        for column in range(numberOfColumns):
            matrix[row].append(rowdata[column])

    return matrix


def printMatrix(matrix):
    for row in range(len(matrix)):

        for column in range(len(matrix[row])):
            print(format(matrix[row][column], "5d"), end=" ")

        print()


def fillMatrixRandomly(numberOfRows, numberOfColumns):
    matrix = []

    for row in range(numberOfRows):

        matrix.append([])

        for column in range(numberOfColumns):
            matrix[row].append(random.randint(0, 99))

    return matrix


def generateZeroMatrix(numberOfRows, numberOfColumns):
    matrix = [[0 for i in range(numberOfRows)] for j in range(numberOfColumns)]

    return matrix


def addMatrix(A, B):
    C = generateZeroMatrix(len(A), len(A[0]))

    for row in range(len(A)):

        for column in range(len(A[row])):
            C[row][column] = A[row][column] + B[row][column]

    return C


def subtractMatrix(A, B):
    C = generateZeroMatrix(len(A), len(A[0]))

    for row in range(len(A)):

        for column in range(len(A[row])):
            C[row][column] = A[row][column] + B[row][column]

    return C


def maxOfElements(A):
    max_val = A[0][0]

    for i in range(len(A)):

        for j in range(len(A[i])):
            max_val = max(max_val, A[i][j])

    return max_val


def transpose(A):
    B = generateZeroMatrix(len(A), len(A[0]))

    for i in range(len(A)):

        for j in range(len(A[i])):
            B[i][j] = A[j][i]

    return B


def multiplyMatrix(A, B):
    C = generateZeroMatrix(len(A), len(B[0]))

    for i in range(len(A)):

        for j in range(len(B[0])):

            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]

    return C


def main():
    sys.stdout = open('output.txt', 'w')
    print("\nReading data from inputs.txt file in current directory\n")
    f = open("inputs.txt", "r")


    line = f.readline()
    numberOfRows, numberOfColumns = [int(x) for x in line.split(' ')]
    A = readMatrix(numberOfRows, numberOfColumns, f)
    print(" *** Matrix A *** ")
    printMatrix(A)
    line = f.readline()

    numberOfRows, numberOfColumns = [int(x) for x in line.split(' ')]
    B = readMatrix(numberOfRows, numberOfColumns, f)
    print(" *** Matrix B *** ")
    printMatrix(B)
    line = f.readline()

    numberOfRows, numberOfColumns = [int(x) for x in line.split(' ')]
    C = readMatrix(numberOfRows, numberOfColumns, f)
    print(" *** Matrix C *** ")
    printMatrix(C)

    D = fillMatrixRandomly(numberOfRows, numberOfColumns)
    print(" *** Matrix D *** ")
    printMatrix(D)

    print("\n ** Computing S = (A+B)  Transpose(C) + D) - A *** \n")

    T1 = addMatrix(A, B)
    print(" *** MatriX T1 = (A+B) ***")
    printMatrix(T1)

    T2 = transpose(C)
    print("*** Matrix T2 = Transpose(C) ***")
    printMatrix(T2)

    T3 = multiplyMatrix(T1, T2)
    print("*** Matrix T3 =(A+B)  transpose(C) ****")
    printMatrix(T3)

    T4 = addMatrix(T3, D)
    print("*** Matrix T4 =(A+B)  transpose(C)+ D ****")
    printMatrix(T4)

    S = subtractMatrix(T4, A)
    print("*** Matrix S =(A+B)  transpose(C) + D - A ****")
    printMatrix(S)

    max_val = maxOfElements(S)
    print("Maximum Element in S = {} ".format(max_val))

main()

########################################################################################
# Question IV:
# Design a class named Triangle that extends the GeometricObject class given in the textbook. The Triangle class
# contains:
# - Three float data fields named side1, side2, and side3 to denote the three sides of the triangle.
# - A constructor that creates a triangle with the specified side1, side2, and side3 with default values 1.0.
# - The accessor (getter) and mutator (setter) methods for all three data fields.
# - The class should throw a RuntimeError exception if the three given sides cannot form a triangle (If one of
# sides is 0 or less than 0.)
# - A method named getArea() that returns the area of this triangle.
# - A method named getPerimeter() that returns the perimeter of this triangle.
# - A method named __eq__(self, other) that checks whether two triangles are equal of not by comparing
# their three sides. For example, if a triangle has side lengths 4,1,3 and another one has side lengths
# 3,4,1 then they should be accepted equal.
# - A method named __str__() that returns a string description for the triangle.
#
# The __str__() method is implemented as follows:
# return "Triangle: side1 = " + str(side1) + " side2 = " +
# str(side2) + " side3 = " + str(side3)
# Implement the Triangle class. Write a test program that generates triangles with three sides of the triangle, a color,
# and 1 or 0 to indicate whether the triangle is filled. The program should generate three Triangle objects. Two of
# these triangles should have the same side lengths. The program should display triangle’s area, perimeter, color,
# and True or False to indicate whether the triangle is filled or not. The program should also compare triangles with
# each other whether they are equal or not.
########################################################################################



print("\n")
print("********************************************************************************")
print("SOLUTION OF QUESTION IV:")
print("********************************************************************************"),
print("\n")


import math


class Triangle:

    def __init__(self):

        self.side1=1.0

        self.side2=1.0

        self.side3=1.0

    def __init__(self,a,b,c):

        self.side1=a

        self.side2=b

        self.side3=c

        if a<=0 or b<=0 or c<=0:

            raise Exception('RunTimeException')

    def getSide1(self):

        return self.side1

    def getSide2(self):

        return self.side2

    def getSide3(self):

        return self.side3

    def setSide1(self,a):

        if a <= 0:

            raise Exception('RunTimeException')

        self.side1=a

    def setSide2(self,a):

        if a<=0:

            raise Exception('RunTimeException')

        self.side2 = a

    def setSide3(self,a):

        if a <= 0:

            raise Exception('RunTimeException')

        self.side3=a

    def getArea(self):

        S=self.side1+self.side2+self.side3

        S /= 2

        A = math.sqrt(S(S-self.side1)(S-self.side2)*(S-self.side3))

        return A

    def getPerimeter(self):

        return self.side1+self.side2+self.side3

    def eq(self,other):

        temp1= self.side1==other.side1 or self.side1==other.side2 or self.side1==other.side3

        temp2= self.side2==other.side1 or self.side2==other.side2 or self.side2==other.side3

        temp3= self.side3==other.side1 or self.side3==other.side2 or self.side3==other.side3

        return temp1 and temp2 and temp3

    def str(self):

        return "Triangle: side1 = " + str(self.side1) + " side2 = " +str(self.side2) + " side3 = " + str(self.side3)






