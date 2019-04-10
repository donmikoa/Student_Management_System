import os
import platform

global listStd #Created listStd as a Global Variable
stdList = ["Michael", "Daniel", "Tope", "Deji", "Joseph"]  # Student List

def manageStudent():

    x = "#" * 30
    y = "=" * 28
    global bye # making "bye" as a super Global Variable
    bye = "\n {} #\n# ==> Built by <=== #\n# ===> Michael Iyaomolere <=== #\n# {}".format(x, y, y, x)
    # The "Bye" is printing the Goodbye Message

    # Printing the Welcome Message And Options For The Program
    print("""
  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Student Management System	========|
 |======================================================|
  -------------Created by Michael Iyaomolere------------
  
  Enter 1 : To View Student's List
  Enter 2 : TO Add New Student
  Enter 3 : To Search Student
  Enter 4 : To Remove Student
  
        """)

    try:  # Creating Exceptions for Avoiding errors
        # Take input From The User
        userInput = int(input("Please Select one of the Options Above"))
    except ValueError:
        exit("\n That's not a Number")  # Error Message
    else:
        print("\n")  # Print New Line






