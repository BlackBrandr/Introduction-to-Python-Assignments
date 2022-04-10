#########################################################################################
# Name: Burak Karataş
# Student ID: 64200045
# Department: Computer Engineering
#
# Assignment ID: A3
########################################################################################
#########################################################################################
# QUESTION I
# Description:
# Write a class that implements Student class that is described in UML diagram given below. Write a
# test program that will generate at least 3 accounts and test each method that you write.
#
#
#########################################################################################
print("\n")
print("SOLUTION OF QUESTION I:")
print("********************************************************************************")

class Student:
    numCourses = 0
    courses = []
    grades = []

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def toString(self):
        return (self.name + "(" + self.address + ")")

    def addCourseGrade(self, course, grade):
        self.courses.append(course)
        self.grades.append(grade)

    def printGrades(self):
        print(self.name, end=" ")
        for i in range(len(self.courses)):
            if (i == len(self.courses) - 1):
                print(self.courses[i] + ":" + str(self.grades[i]))
            else:
                print(self.courses[i] + ":" + str(self.grades[i]), end=", ")

    def getAverageGrade(self):
        sum = 0
        c = 0
        for i in self.grades:
            sum += i
            c += 1
        return (sum / c)

s1 = Student("Burak", "Sultangazi / İstanbul / Türkiye")
s2 = Student("Emre",  "Terkos / İstanbul / Türkiye")
s3 = Student("Ziya", "Küçükköy / İstanbul / Türkiye")

print(s1.getName())
print(s1.getAddress())
s1.setAddress("Sultangazi")
print(s1.toString())
s1.addCourseGrade("A", 95)
s1.addCourseGrade("B", 85)
s1.addCourseGrade("C", 60)
print(s1.getAverageGrade)
s1.printGrades()

print(s2.getName())
print(s2.getAddress())
s2.setAddress("Sultangazi")
print(s2.toString())
s2.addCourseGrade("A", 94)
s2.addCourseGrade("B", 86)
s2.addCourseGrade("C", 61)
print(s2.getAverageGrade)
s2.printGrades()

print(s3.getName())
print(s3.getAddress())
s3.setAddress("Sultangazi")
print(s3.toString())
s3.addCourseGrade("A", 93)
s3.addCourseGrade("B", 87)
s3.addCourseGrade("C", 63)
print(s3.getAverageGrade)
s3.printGrades()


#########################################################################################
# QUESTION II
# Description:
# Write a function that parses a binary number into a hexadecimal and decimal number. The function
# header is:
# def binaryToHexDec(binaryValue):
# Before conversion, the program should check its input. The input should be a binary number that
# only contains 0s and1s. The function returns hexadecimal, decimal and octal representations of the
# binary number as follows:
# hexVal, decVal, octal = binaryToHexDec(“1111011”)
#
# Write a test program that prompts the user to enter binary numbers and displays the corresponding
# hexadecimal, decimal, and octal values.
#
#########################################################################################

print("********************************************************************************")
print("\n")
print("SOLUTION OF QUESTION II:")
print("********************************************************************************")

def converter():
    n = (input("Please enter binary number: "))
    s = int(n, 2)
    print("The binary value of", n,"is", s, "in decimal")
    n = int(n)
    print("The binary value of", n, "is",oct(n), "in octal.")
    print("The binary value of", n, "is",hex(n), "in hexadecimal.")

converter()


#########################################################################################
# QUESTION III
# Description:
# Write a number guessing game as shown in the Figure below. The program shall generate a random
# number between 1 to 100. It shall mask out the random number generated and output "Try Higher" or
# "Try Lower" depending on the user’s input. When your guess is right, it will display a message box
# with a message "Yot Got it".
#
#########################################################################################

print("********************************************************************************")
print("\n")
print("SOLUTION OF QUESTION III:")
print("********************************************************************************")


from tkinter import *
import random

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.widgets()
        self.number_pick()
        self.number_of_tries()

    def widgets(self):
        Label(self, text = 'Guess the number'
              ).grid(row = 0, column = 1, columnspan = 2, sticky = N)
        Label(self, text = 'I am thinking of a number between 1 and 100'
              ).grid(row = 1, column = 0, columnspan = 3, sticky = W)
        Label(self, text = 'Try to guess in as few attempts as possible'
              ).grid(row = 2, column = 0, columnspan = 3, sticky = W)
        Label(self, text = 'I will tell you to go higher or lower after each guess'
              ).grid(row = 3, column = 0, columnspan = 3, sticky = W)
        Label(self, text = 'Your guess: '
              ).grid(row = 4, column = 0, sticky = W)
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row = 4, column = 1, sticky = W)
        self.guess_ent.focus()
        Label(self, text = ' number of tries: '
              ).grid(row = 5, column = 0, sticky = W)
        self.no_tries_txt = Text(self, width = 2, height = 1, wrap = NONE)
        self.no_tries_txt.grid(row = 5, column = 1, sticky = W)
        Button(self, text = 'Guess', command = self.check_if_correct
               ).grid(row = 5, column = 2, sticky = W)
        self.result_txt = Text(self, width = 80, height = 15, wrap = WORD)
        self.result_txt.grid(row = 6, column = 0, columnspan = 4)

    def number_pick(self):
        self.rand_number = random.randint(1, 100)
        print(self.rand_number)

    def check_if_correct(self):
        self.result = ""
        gnum = self.guess_ent.get()
        gnum = int(gnum)

        if gnum == self.rand_number:
            gnum = str(gnum)
            self.result = gnum + "  is the true number!\n"
            self.tries += 1
        elif gnum < self.rand_number:
            gnum = str(gnum)
            self.result = gnum + " is too low, Guess higher.\n"
            self.tries += 1
        elif gnum > self.rand_number:
            gnum = str(gnum)
            self.result = gnum + " is too high, Guess lower.\n"
            self.tries += 1

        self.give_result()
        print(self.tries)

    def number_of_tries(self):
        self.tries = 0

    def give_result(self):
        self.result_txt.delete(0.0, END)
        self.result_txt.insert(0.0, self.result)
        self.no_tries_txt.delete(0.0, END)
        self.no_tries_txt.insert(0.0, self.tries)

root = Tk()
root.title('Guess the Number')
app = Application(root)
root.mainloop()


#########################################################################################
# QUESTION IV
# Description:
# Write a GUI calculator application that works like a Windows 10 standard calculator. You should
# implement the functionality of every button except the history button.
#
#########################################################################################

print("********************************************************************************")
print("\n")
print("SOLUTION OF QUESTION IV:")
print("********************************************************************************")

from tkinter import *


full_stop = 1
left_bracket = 0
for_calculation = None



def button(parent, text, font, bg, width, pad=1):
    btn = Button(parent, text=text, font=font, bg=bg, width=width, height=2, relief=FLAT, bd=0, padx=pad)
    return btn


def zero(event=""):
    if expression.get().startswith("0") and len(expression.get()) == 1:
        expression.set("")
    if len(expression.get()) < 30:
        expression.set(expression.get() + "0")


def one(event=""):
    if expression.get().startswith("0") and len(expression.get()) == 1:
        expression.set("")
    if len(expression.get()) < 30:
        expression.set(expression.get() + "1")



def two(event=""):
    if expression.get().startswith("0") and len(expression.get()) == 1:
        expression.set("")
    if len(expression.get()) < 30:
        expression.set(expression.get() + "2")



def three(event=""):
    if expression.get().startswith("0") and len(expression.get()) == 1:
        expression.set("")
    if len(expression.get()) < 30:
        expression.set(expression.get() + "3")



def four(event=""):
    if expression.get().startswith("0") and len(expression.get()) == 1:
        expression.set("")
    if len(expression.get()) < 30:
        expression.set(expression.get() + "4")



def five(event=""):
    if expression.get().startswith("0") and len(expression.get()) == 1:
        expression.set("")
    if len(expression.get()) < 30:
        expression.set(expression.get() + "5")



def six(event=""):
    if expression.get().startswith("0") and len(expression.get()) == 1:
        expression.set("")
    if len(expression.get()) < 30:
        expression.set(expression.get() + "6")



def seven(event=""):
    if expression.get().startswith("0") and len(expression.get()) == 1:
        expression.set("")
    if len(expression.get()) < 30:
        expression.set(expression.get() + "7")



def eight(event=""):
    if expression.get().startswith("0") and len(expression.get()) == 1:
        expression.set("")
    if len(expression.get()) < 30:
        expression.set(expression.get() + "8")



def nine(event=""):
    if expression.get().startswith("0") and len(expression.get()) == 1:
        expression.set("")
    if len(expression.get()) < 30:
        expression.set(expression.get() + "9")





def add(event=""):
    global full_stop
    if len(expression.get()) < 30 and not expression.get().endswith("."):
        if expression.get().endswith("+"):
            expression.set(expression.get()[:-1] + "+")
        elif expression.get().endswith("-"):
            expression.set(expression.get()[:-1] + "+")
        elif expression.get().endswith("x"):
            expression.set(expression.get()[:-1] + "+")
        elif expression.get().endswith("÷"):
            expression.set(expression.get()[:-1] + "+")
        else:
            expression.set(expression.get() + "+")
        full_stop = 1



def subtract(event=""):
    global full_stop
    if len(expression.get()) < 30 and not expression.get().endswith("."):
        if expression.get().endswith("+"):
            expression.set(expression.get()[:-1] + "-")
        elif expression.get().endswith("-"):
            expression.set(expression.get()[:-1] + "-")
        elif expression.get().endswith("x"):
            expression.set(expression.get()[:-1] + "-")
        elif expression.get().endswith("÷"):
            expression.set(expression.get()[:-1] + "-")
        else:
            expression.set(expression.get() + "-")
        full_stop = 1



def multiply(event=""):
    global full_stop
    if len(expression.get()) < 30 and not expression.get().endswith("."):
        if expression.get().endswith("+"):
            expression.set(expression.get()[:-1] + "x")
        elif expression.get().endswith("-"):
            expression.set(expression.get()[:-1] + "x")
        elif expression.get().endswith("x"):
            expression.set(expression.get()[:-1] + "x")
        elif expression.get().endswith("÷"):
            expression.set(expression.get()[:-1] + "x")
        else:
            expression.set(expression.get() + "x")
        full_stop = 1


def divide(event=""):
    global full_stop
    if len(expression.get()) < 30 and not expression.get().endswith("."):
        if expression.get().endswith("+"):
            expression.set(expression.get()[:-1] + "÷")
        elif expression.get().endswith("-"):
            expression.set(expression.get()[:-1] + "÷")
        elif expression.get().endswith("x"):
            expression.set(expression.get()[:-1] + "÷")
        elif expression.get().endswith("÷"):
            expression.set(expression.get()[:-1] + "÷")
        else:
            expression.set(expression.get() + "÷")
        full_stop = 1




def point(event=""):
    global full_stop
    if len(expression.get()) < 30 and full_stop == 1:
        if not expression.get().endswith(("+", "-", "x", "÷", "(", ")")):
            expression.set(expression.get() + ".")
            full_stop = 0


def left(event=""):
    global left_bracket
    if expression.get() == "0":
        expression.set("(")
    else:
        expression.set(expression.get() + "(")
    left_bracket += 1



def right(event=""):
    global left_bracket
    if left_bracket != 0 and not expression.get() == "0":
        expression.set(expression.get() + ")")
        left_bracket -= 1



def reverse():
    if not expression.get().startswith("-") and not expression.get().startswith("0") and len(expression.get()) < 30:
        expression.set("-" + expression.get())
    elif expression.get().startswith("-"):
        expression.set(expression.get()[1:])



def delete(event=""):
    expression.set(expression.get()[:-1])
    if expression.get() == "":
        expression.set("0")



def reset(event=""):
    global for_calculation
    expression.set("0")
    for_calculation = None
    calculated.set("")



def calculate(event=""):
    global for_calculation
    for_calculation = expression.get().replace("x", "*").replace("÷", "/")
    calculated.set(eval(for_calculation))
    if str(calculated.get()[int(len(calculated.get()) - 2):]) == ".0":
        calculated.set(calculated.get()[:-2])
    expression.set("0")


root = Tk()
root.title("CALCULATOR")
root.geometry("443x405")
root.iconbitmap("icon.ico")
root.resizable(0, 0)
root.configure(bg="#D9D9D9")





expression = StringVar(root, "0")
calculated = StringVar(root)


expression_txt = Entry(root, textvariable=expression, justify=RIGHT, selectbackground="#D9D9D9",
                       font="Comic-sens 15 bold", selectforeground="#000000", readonlybackground="#D9D9D9", relief=FLAT,
                       bd=0, state="readonly")
expression_txt.pack(pady=5, anchor=N, padx=2, fill=X)


calculated_lbl = Label(root, textvariable=calculated, anchor=E, bg="#D9D9D9", relief=FLAT, bd=0,
                       font="Comic-sens 20 bold")
calculated_lbl.pack(pady=5, anchor=N, padx=6, fill=X)



frame1 = Frame(root, bg="#D9D9D9")

btn = button(frame1, "CE", "Calibri 15", "#EEEEEE", 10)  # 1
btn.config(command=reset)
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

btn = button(frame1, "±", "Calibri 15", "#EEEEEE", 10)  # 2
btn.config(command=reverse)
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

btn = button(frame1, "C", "Calibri 15", "#EEEEEE", 10)  # 3
btn.config(command=delete)
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

btn = button(frame1, "÷", "Calibri 15", "#EEEEEE", 10)  # 4
btn.config(command=divide)
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

frame1.pack(side=TOP, anchor=NW, padx=5, fill=BOTH)


frame2 = Frame(root, bg="#D9D9D9")

btn = button(frame2, "7", "Calibri 15 bold", "#FFFFFF", 10)  # 1
btn.config(command=seven)
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

btn = button(frame2, "8", "Calibri 15 bold", "#FFFFFF", 10)  # 2
btn.config(command=eight)
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

btn = button(frame2, "9", "Calibri 15 bold", "#FFFFFF", 10)  # 3
btn.config(command=nine)
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

btn = button(frame2, "x", "Calibri 15", "#EEEEEE", 10)  # 4
btn.config(command=multiply)
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

frame2.pack(side=TOP, anchor=NW, padx=5, fill=BOTH)


frame3 = Frame(root, bg="#D9D9D9")

btn = button(frame3, "4", "Calibri 15 bold", "#FFFFFF", 10)  # 1
btn.config(command=four)
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

btn = button(frame3, "5", "Calibri 15 bold", "#FFFFFF", 10)  # 2
btn.config(command=five)
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

btn = button(frame3, "6", "Calibri 15 bold", "#FFFFFF", 10)  # 3
btn.config(command=six)
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

btn = button(frame3, "-", "Calibri 15", "#EEEEEE", 10)  # 4
btn.config(command=subtract)
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

frame3.pack(side=TOP, anchor=NW, padx=5, fill=BOTH)


frame4 = Frame(root, bg="#D9D9D9")

btn = button(frame4, "1", "Calibri 15 bold", "#FFFFFF", 10)  # 1
btn.config(command=one)
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

btn = button(frame4, "2", "Calibri 15 bold", "#FFFFFF", 10)  # 2
btn.config(command=two)
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

btn = button(frame4, "3", "Calibri 15 bold", "#FFFFFF", 10)  # 3
btn.config(command=three)
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

btn = button(frame4, "+", "Calibri 15", "#EEEEEE", 10)  # 4
btn.config(command=add)
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

frame4.pack(side=TOP, anchor=NW, padx=5, fill=BOTH)


frame5 = Frame(root, bg="#D9D9D9")

btn = button(frame5, "(", "Calibri 15", "#EEEEEE", 4, pad=4)  # 1
btn.config(command=left)
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

btn = button(frame5, ")", "Calibri 15", "#EEEEEE", 4, pad=4)  # 2
btn.config(command=right)
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

btn = button(frame5, "0", "Calibri 15 bold", "#FFFFFF", 10)  # 3
btn.config(command=zero)
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

btn = button(frame5, ".", "Calibri 15", "#EEEEEE", 10)  # 4
btn.config(command=point)
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

btn = button(frame5, "=", "Calibri 15 bold", "#AEDB9F", 10)  # 5
btn.config(command=calculate)
btn.pack(side=LEFT, padx=1, pady=1, fill=BOTH)

frame5.pack(side=TOP, anchor=NW, padx=5, fill=BOTH)


root.bind('0', zero)
root.bind('1', one)
root.bind('2', two)
root.bind('3', three)
root.bind('4', four)
root.bind('5', five)
root.bind('6', six)
root.bind('7', seven)
root.bind('8', eight)
root.bind('9', nine)
root.bind('+', add)
root.bind('-', subtract)
root.bind('*', multiply)
root.bind('/', divide)
root.bind('.', point)
root.bind('(', left)
root.bind(')', right)
root.bind('<BackSpace>', delete)
root.bind('<Delete>', reset)
root.bind('<Return>', calculate)


root.mainloop()


