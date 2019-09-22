# File : Assignment 2.1.py
# Name : Gourav Verma
# Date : 9/6/2019
# Course : DSC-510 - Introduction to Programming
# Des  : Week-2 : Python Variables and Math Operations
A = '*'
print(A * 100)
print("This program is to calculate cost of installing fiber optics cable : "
      "Installation charges $0.87/Feet")              # Welcome message
print(A * 100)
# Take inputs from user
comp = input('What is the name of your Company? : ')
len = input('How many feet of Fiber Optics Cable you want to install? : ')
# Check if length entered is an integer, otherwise show error
try:
    len = int(len)                                    # Is length integer?
    cost = len * 0.87                                 # Yes, calculate cost
    print(A * 14, "Receipt", A * 14)
    print("Name of Company         : ", comp)         # Print company name
    print("Length of Fibre Cable   : ", len, "feet")  # Print length of cable
    print("Total Installation Cost : ", "$", cost)    # Print cost
    print(A * 37)
except:
    print("Error : Please enter only integer length of cable..!!")  # Show error for bad input length


