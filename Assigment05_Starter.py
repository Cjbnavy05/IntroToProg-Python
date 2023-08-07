# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Chris Boyle, 08/07/2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection
count = 0

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
try:
    objFile = open("ToDoList.txt", "r")

    for row in objFile:
        lstRow = row.split(",")
        dicRow = {"Task": lstRow[0], "Priority": lstRow[1]}
        lstTable.append(dicRow)
        print(lstRow[0] + '|' + lstRow[1].strip())
    objFile.close()
except:
    print('File not found, will make a new file when you save')

objFile = open("ToDoList.txt", 'a')
objFile = open("ToDoList.txt", 'r')
row = objFile.readline()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Task | Priority ")
        for i in lstTable:
            taskN = i["Task"]
            taskP = i["Priority"]
            print(str(taskN) + " | " + taskP)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        strItem = input("Task:  ")
        strValue = input("Priority:  ")
        lstTable.append({"Task": strItem, "Priority": strValue})
        strChoice = input("Exit? ('y/n'): ")
        if strChoice.lower() == 'y':
            break
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        print("# | Task | Priority")
        for i in lstTable:
            count += 1
            taskN = i["Task"]
            taskP = i["Priority"]
            print(str(count) + " | " + str(taskN) + " | " + taskP)
        delRow = input("Choose which to delete: ")
        lstTable.pop(int(delRow) - 1)
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(str(row["Task"]) + ',' + str(row["Priority"] +'\n'))
        objFile.close()
        print("Now in file!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        strChoice = input("Exit? ('y/n'): ")
        if strChoice.lower() == 'y':
            break  # and Exit the program
