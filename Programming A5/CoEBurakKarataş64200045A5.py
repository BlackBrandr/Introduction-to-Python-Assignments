#########################################################################################
# Name: Burak Karataş
# Student ID: 63200045
# Department: Computer Engineering
#
# Assignment ID: A5
########################################################################################
# Question 1:
# Write a function that prompts the user to enter an input filename and an output filename and saves the
# encrypted version of the input file to the output file. Encode the file by
# - insert a new character “x” after 7 characters,
# - adding 2 to every byte in the input file except for characters a, i, e, o, u,
# - replace characters a, i, e, o, u by 1,2,3,4,5
# b. Write a function to decode the encrypted file. Your program should prompt the user to enter an input
# filename and an output filename and should save the unencrypted version of the input file to the output
# file.
########################################################################################

print("\n")
print("********************************************************************************")
print("SOLUTION OF QUESTION I:")
print("********************************************************************************")

def encrypt():
    plain = input("Enter input filename: ")
    cipher = input("Enter output filename: ")
    ret = ""
    vowel = "aieou"
    with open(plain) as f:
        for i,j in enumerate(f.read().lower()):
            if j in vowel:
                ret += str(vowel.index(j)+1)
            else:
                ret += chr(ord(j)+2)
            if (i+1)%7==0:
                ret+="x"
    with open(cipher,'w') as f:
        f.write(ret)

def decrypt():
    cipher = input("Enter input filename: ")
    plain = input("Enter output filename: ")
    ret = ""
    num = {
        '1' : 'a',
        '2' : 'i',
        '3' : 'e',
        '4' : 'o',
        '5' : 'u'
    }
    with open(cipher) as f:
        for i,j in enumerate(f.read().lower()):
            if (i+1)%8==0:
                continue
            if j in "12345":
                ret += num[j]
            else:
                ret += chr(ord(j)-2)
    with open(plain,'w') as f:
        f.write(ret)

encrypt()
decrypt()


########################################################################################
# Question II:
# Write a program that reads in a Python source code file and counts the occurrence of each identifier
# (variables, class, and method names) in the file using a dictionary. Another dictionary is used to
# positions of identifiers with a list in the file. Your program should prompt the user to enter the
# Python source code filename and then construct these two dictionaries. After reading the entire file,
# the program should display the contents two dictionaries.
########################################################################################

print("\n")
print("********************************************************************************")
print("SOLUTION OF QUESTION II:")
print("********************************************************************************")


s = input("Enter name of the source file: ")
f = open(s)
s = f.read()
d = {}
p = {}
l = len(s)
i = 0
while i<l:
    j = i
    if (ord(s[j])>=48 and ord(s[j])<=57):
        i+=1
        continue
    while j<l and ((ord(s[j])>=97 and ord(s[j])<=122) or (ord(s[j])>=65 and ord(s[j])<=90) or (ord(s[j])>=48 and ord(s[j])<=57) or (ord(s[j])==95)):
        j+=1
    if i==j:
        i+=1
        continue
    if s[i:j] in d:
        d[s[i:j]]+=1
        p[s[i:j]].append(i)
    else:
        d.setdefault(s[i:j],1)
        p.setdefault(s[i:j],[i])
    i = j+1
f.close()
print()
print("dictCounts: ")
print()
print(d)
print()
print("dictPositions: ")
print()
print(p)

########################################################################################
# Question III:
# Write a program that creates an exception class called NumberOutOfRangeException (derived from RuntimeError),
# designed to be thrown when a number is discovered that has a value x not in range 1000 < x < 2000. In the main
# driver of the program, read number from the user until the user enters -1000. If a number is entered that is not in the
# range, throw the exception. Allow the thrown exception to terminate the program.
########################################################################################

print("\n")
print("********************************************************************************")
print("SOLUTION OF QUESTION III:")
print("********************************************************************************")

class NumberOutOfRangeException(RuntimeError):

    def __init__(self, value):

        self.value = value

    def __str__(self):
        return (repr(self.value))

def main():
    try:
        while (True):
            num = int(input("Enter a number: "))
            if num == -1000:
                break
            if num < 1000 or num > 2000:
                raise NumberOutOfRangeException(num)
    except NumberOutOfRangeException as e:
        print("{} is not in range 1000 to 2000".format(e.value))

main()

########################################################################################
# Question IV:
#
# The recursive sorting technique called quicksort uses the following basic algorithm for a one-
# dimensional array of values:
#
#a) Partitioning Step: Take the first element of the unsorted array and determine its final location in
# the sorted array (i.e., all values to the left of the element in the array are less than the element, and all
# values to the right of the element in the array are greater than the element—we show how to do this
# below). We now have one element in its proper location and two unsorted subarrays.
# b) Recursive Step: Perform Step 1 on each unsorted subarray. Each time Step 1 is performed on a
# subarray, another element is placed in its final location of the sorted array, and two unsorted
# subarrays are created. When a subarray consists of one element, that element is in its final location
# (because a one-element array is already sorted).
# The basic algorithm seems simple enough, but how do we determine the final position of the first
# element of each subarray? As an example, consider the following set of values (the element in bold is
# the partitioning element—it will be placed in its final location in the sorted array):
#37 2 6 4 89 8 10 12 68 45
# Starting from the rightmost element of the array, compare each element with 37 until an element less
# than 37 is found; then swap 37 and that element. The first element less than 37 is 12, so 37 and 12 are
# swapped. The new array is
# 12 2 6 4 89 8 10 37 68 45
# Element 12 is in italics to indicate that it was just swapped with 37. Starting from the left of the
# array, but beginning with the element after 12, compare each element with 37 until an element
# greater than 37 is found—then swap 37 and that element. The first element greater than 37 is 89, so
# 37 and 89 are swapped. The new array is
# 12 2 6 4 37 8 10 89 68 45
# Starting from the right, but beginning with the element before 89, compare each element with 37
# until an element less than 37 is found—then swap 37 and that element. The first element less than 37
# is 10, so 37 and 10 are swapped. The new array is
# 12 2 6 4 10 8 37 89 68 45
# Starting from the left, but beginning with the element after 10, compare each element with 37 until an
# element greater than 37 is found—then swap 37 and that element. There are no more elements
# greater than 37, so when we compare 37 with itself, we know that 37 has been placed in its final
# location in the sorted array. Every value to the left of 37 is smaller than it, and every value to the
# right of 37 is larger than it.
# Once the partition has been applied on the previous array, there are two unsorted subarrays. The
# subarray with values less than 37 contains 12, 2, 6, 4, 10 and 8. The subarray with values greater than
# 37 contains 89, 68 and 45. The sort continues recursively, with both subarrays being partitioned in
# the same manner as the original array. Based on the preceding discussion, write recursive function
# quick_sort_helper to sort a one-dimensional integer array. The function should receive as arguments
# a starting index and an ending index on the original array being sorted. Call this function from a
# quick_sort function that receives just the original array to sort. At each recursive call, print the
# parameters of the recursive method call and array(list) contents.
########################################################################################

print("\n")
print("********************************************************************************")
print("SOLUTION OF QUESTION IV:")
print("********************************************************************************")

def partition(Array, start, end):
    pos = start
    for i in range(start, end):
        if Array[i] < Array[end]:
            Array[i],Array[pos] = Array[pos],Array[i]
            pos += 1
    Array[pos],Array[end] = Array[end],Array[pos]
    return pos

def quick_sort_helper(Array, start, end):
    print('start:',start,' end:',end,' Array:',Array)
    if start < end:
        pos = partition(Array, start, end)
        quick_sort_helper(Array, start, pos - 1)
        quick_sort_helper(Array, pos + 1, end)

def quick_sort(Array):
        start = 0
        end = len(Array)-1
        quick_sort_helper(Array,start,end)
Array= [37,2,6,4,89,8,10,12,68,45]
quick_sort(Array)
print('Final sorted Array: ',Array)
