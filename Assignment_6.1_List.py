# File : Assignment 6.1.py
# Name : Gourav Verma
# Date : 10/04/2019
# Course : DSC-510 - Introduction to Programming
# Des  : Week-6 : List

import sys
temperatures = []
num = 0

def userinput():
    try:
        while True:
            num = input()
            temperatures.append(float(num))
    except:
        if num == "stop":
            return temperatures
        else:
            sys.exit("Bad input.. Try Again..")       # exit in case of bad input

# Main Body
print("Input a range of Temperatures in Farenheight:"
      "\n*************Type 'stop' to end**************")
userinput()

# Print Outputs
print("List of temperatures is : ", temperatures)
print("Total number of Temperatures is : ", len(temperatures))
print("Maximum Temperature is : ", max(temperatures), "\u00b0F")
print("Minimum Temperature is : ", min(temperatures), "\u00b0F")

