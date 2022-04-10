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