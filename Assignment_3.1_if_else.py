# File : Assignment 3.1.py
# Name : Gourav Verma
# Date : 9/14/2019
# Course : DSC-510 - Introduction to Programming
# Des  : Week-3 : Conditional Execution
import sys
A = '*'
print(A * 101)
print("This program is to calculate cost of installing fiber optics cable : "
      "Installation charges $0.87/Feet*\n"
      "*Discounts on Bulk Orders")              # Welcome message
print(A * 101)
# Take inputs from user
comp = input('What is the name of your Company? : ')
len = input('How many feet of Fiber Optics Cable you want to install? : ')
# Check if length entered is an integer, otherwise show error
try:
    len = int(len)  # Is length integer?
except:
    sys.exit("Error : Please enter only integer length of cable..!!")  # Show error for bad input length
else:
    if (len > 500):
        price = 0.50
        cost = len * 0.50
    elif (len > 250):
        price = 0.70
        cost = len * 0.70
    elif (len > 100):
        price = 0.80
        cost = len * 0.80
    else:
        price = 0.87
        cost = len * 0.87    # calculate cost

B_cost = len * 0.87
print(A * 14, "Receipt", A * 14)
print("Name of Company         : ", comp)  # Print company name
print("Length of Fibre Cable   : ", len, "feet")  # Print length of cable
print("Total Installation Cost : ", "$", round(B_cost, 2))  # Total Price per feet
print("Price applied /feet     : ", "$", price)  # Price per feet
print("Discount Applied        : ", "-$", round(B_cost - cost, 2))   # Discount applied
print(A * 37)
print("Final Installation Cost : ", "$", round(cost, 2))  # Print cost
print(A * 37)