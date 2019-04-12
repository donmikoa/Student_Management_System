import os
import platform

global stdList  # Created stdList as a Global Variable
stdList = ["Michael", "Daniel", "Tope", "Deji", "Joseph"]  # Student List

def application():

    x = "#" * 30
    y = "=" * 28
    global bye # making "bye" as a super Global Variable
    bye = "\n {} #\n# ==> Built by <=== #\n# ===> Michael Iyaomolere <=== #\n# {} #\n{}".format(x, y, y, x)
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

    #  Checking What User Inputed
    if userInput == 1:
        print ("Student's List\n")
        for students in stdList:
            print("=>{}".format(students))

    elif userInput == 2:  # Option To Add A New Student To The List
        newStd = input("Enter New Student: ")
        if newStd in stdList:  # To Check Tht Presence Of The Student's Name On The List
            print("\nThis student {} Is Already In The System".format(newStd))
        else:
            stdList.append(newStd)
            print("\n==> New Student {} Has Been Added\n".format(newStd))
            for students in stdList:
                print("=> {}".format(students))

    elif userInput == 3:  # Input To Search Students Present In The List
        srcStd = input("Enter Student Name To Be Searched")
        if srcStd in stdList: # The Condition To Search For The Student
            print("\n=> Record Found Of Student {}".format(srcStd))
        else:
            print("\n=> No Record Found Of Student {}".format(srcStd))  # Error Message

    elif userInput == 4: # Option To Remove A Student Name From The List
        rmStd = input("Enter Student Name To Be Removed")
        if rmStd in stdList:  # To Check Tht Presence Of The Student's Name On The List
            stdList.remove(rmStd)
            print("\n=> Student {} Successfully Deleted \n".format(rmStd))
            for students in stdList
                print("=> {}".format(students))
        else:
            print("\n=> No Record Of Student {} Fount".format(rmStd))  #Error Message


















