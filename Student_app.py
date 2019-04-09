import os
import platform

global listStd #Created listStd as a Global Variable
listStd = ["Michael", "Daniel", "Tope", "Deji", "Joseph"]  # List Of Students

def manageStudent():

    x = "#" * 30
    y = "=" * 28
    global bye # making "bye" as a super Global Variable
    bye = "\n {} #\n# ==> Brought To You By <=== #\n# ===> Mikoa Inc. <=== #\n# {}".format(x, y, y, x)
    # The "Bye" is printing the Goodbye Message

    # Printing the Welcome Message And Options For The Program
    print("""
    ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Student Management System	========|
 |======================================================|
  -----------------Powered by Mikoa Inc.----------------
  
  Enter 1 : To View Student's List
  Enter 2 : TO Add New Student
  Enter 3 : To Search Student
  Enter 4 : To Remove Student
  
        """)

    try: # Creating Exceptions for Avoiding errors
        userInput = int(input("Pl"))