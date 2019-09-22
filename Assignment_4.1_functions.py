# File : Assignment 4.1.py
# Name : Gourav Verma
# Date : 9/14/2019
# Course : DSC-510 - Introduction to Programming
# Des  : Week-4 : Functions
import sys

A = '*'
print(A * 101)
print("This program is to calculate cost of installing fiber optics cable : "
      "Installation charges $0.87/Feet*\n"
      "*Discounts on Bulk Orders")  # Welcome message
print(A * 101)
# Take inputs from user
comp = input('What is the name of your Company? : ')
lnth = input('How many feet of Fiber Optics Cable you want to install? : ')


# Check if length entered is an integer, otherwise show error
def fn_cost(lnth, price=0.87):
    cost = lnth * price
    b_cost = lnth * 0.87
    print(A * 14, "Receipt", A * 14)
    print("Name of Company         : ", comp)  # Print company name
    print("Length of Fibre Cable   : ", lnth, "feet")  # Print length of cable
    print("Total Installation Cost : ", "$", round(b_cost, 2))  # Total Price per feet
    print("Price applied /feet     : ", "$", price)  # Price per feet
    print("Discount Applied        : ", "-$", round(b_cost - cost, 2))  # Discount applied
    print(A * 37)
    print("Final Installation Cost : ", "$", round(cost, 2))  # Print cost
    print(A * 37)


try:
    lnth = int(lnth)  # Is length integer?
except:
    sys.exit("Error : Please enter only integer length of cable..!!")  # Show error for bad input length
else:
    if lnth > 500:
        fn_cost(lnth, 0.50)
    elif lnth > 250:
        fn_cost(lnth, 0.70)
    elif lnth > 100:
        fn_cost(lnth, 0.80)
    else:
        fn_cost(lnth)
