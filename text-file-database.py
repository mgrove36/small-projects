# math used for rounding down
import math

# add new user's info to end of file
def insert(lines):
    print("ID:", math.floor(len(lines)/3))
    lines.append(input("Name: ") + " \n")
    lines.append(input("Age: ") + " \n")
    lines.append(input("School year: ") + " \n")
    return lines

# remove user's info from file, by user ID
def delete(lines):
    id = input("ID: ")
    for i in range(math.floor(len(lines)/3)):
        if i == id:
            lines.pop(i*3)
            lines.pop(i*3)
            lines.pop(i*3)
    return lines

# print a user's info from file, by user ID
def select(lines):
    id = input("ID: ")
    for i in range(math.floor(len(lines)/3)):
        if i == id:
            print("Name:", lines[id*3].strip(" \n") + ", age:", lines[id*3+1].strip(" \n") + ", school year:", lines[id*3+2].strip(" \n"))
        else:
            print("ID not found")

# replace a user's info in file, by user ID
def replace(lines):
    id = input("ID: ")
    for i in range(math.floor(len(lines)/3)):
        if i == id:
            print("Name:", lines[id*3] + ", age:", lines[id*3+1] + ", school year:", lines[id*3+2])
            lines.insert(i*3, input("School year: ") + " \n")
            lines.insert(i*3, input("Age: ") + " \n")
            lines.insert(i*3, input("Name: ") + " \n")
        else:
            print("ID not found")
    for i in range(math.floor(len(lines)/3)):
        if i == id:
            lines.pop(i*3)
            lines.pop(i*3)
            lines.pop(i*3)
    return lines

# attempt to open file
try:
    file = open("data.txt","r+")
# if file doesn't exist, create it
except:
    file = open("data.txt","w+")
# read the lines from the file
lines = file.readlines()
# run until user chooses to exit
while True:
    # print each user's info, one user per line
    for i in range(math.floor(len(lines)/3)):
        # only print the content if the file isn't empty
        if len(lines) > 2:
            print("\n" + str(i) + " - name:", lines[i*3].strip(" \n") + ", age:", lines[i*3+1].strip(" \n") + ", school year:", lines[i*3+2].strip(" \n") + "\n")
    # ask the user which function they want to perform
    function = input("Function (insert, i; delete, d; select, s; replace, r; exit, e): ")
    # add user to file
    if function.strip(" ") == "i":
        lines = insert(lines)
        file.writelines(lines)
    # remove user from file
    elif function.strip(" ") == "d":
        lines = delete(lines)
        file.writelines(lines)
    # print user's info from file
    elif function.strip(" ") == "s":
        select(lines)
    # replace user's info in file
    elif function.strip(" ") == "r":
        lines = replace(lines)
        file.writelines(lines)
    # exit the program by breaking the loop
    elif function.strip(" ") == "e":
        break
# close the file
file.close()