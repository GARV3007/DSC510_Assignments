# File : Assignment 5.1.py
# Name : Gourav Verma
# Date : 9/27/2019
# Course : DSC-510 - Introduction to Programming
# Des  : Week-5 : Loops

import operator

def performCalculation(op):
    global num1
    global num2
    try:
        num1 = float(input("Enter 1st Number: "))
        try:
            num2 = float(input("Enter 2nd Number: "))
        except ValueError:
            print("Error : Bad Input Number 2nd..!!")
            return None
    except ValueError:
        print("Error : Bad Input Number 1st..!!")
        return None

    try:
        print('Output of operation is: ', op(num1, num2))
        print('End of Operation..!')
    except ZeroDivisionError:
        print("Error : 2nd Number should not be zero for division..!!")
        return None


def calculateAverage():
    try:
        count = int(input("For how many numbers you want to calculate average: "))
    except:
        print("Error : Bad input")
        return None

    tot = 0
    for i in range(count):
        try:
            num = float(input("Enter number: "))
            tot = tot + num
        except ValueError:
            print("Error : Bad input Number..!")
            return None

    print("sum of all is: ", tot)
    print("Avg of all is: ", round(tot/count, 2))
    print('End of Operation..!')

looping = True  # type: bool
A = '*'
while looping == True:
    print(A * 71)
    print("Which operation do you want me to Perform for you?")
    print("Choose from : addition, substraction, multiplication, division, average")
    print("If you wish to exit, type 'end'.")
    print(A * 71)
    operation = input("Enter Operation: ")
    if operation == 'end':
        looping = False
        print("Thank You. GoodBye..!")
    elif operation == 'addition':
        performCalculation(operator.add)
    elif operation == 'substraction':
        performCalculation(operator.sub)
    elif operation == 'multiplication':
        performCalculation(operator.mul)
    elif operation == 'division':
        performCalculation(operator.truediv)
    elif operation == 'average':
        calculateAverage()
    else:
        print("Error : Bad input Operation..! Try Again..! Check for Typo..!")
