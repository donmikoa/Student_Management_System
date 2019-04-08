import os
import platform

global listStd #Created listStd as a Global Variable
listStd = ["Michael", "Daniel", "Tope", "Deji", "Joseph"]  # List Of Students

def manageStudent():

    x = "#" * 30
    y = "=" * 28
    global bye #making "bye" as a super Global Variable
    bye = "\n {} #\n# ==> Brought To You By <=== #\n# ===> Miikoa Inc. <=== #\n# {}".format(x, y, y, x)
    # The "Bye" is printing the Goodbye Message
    