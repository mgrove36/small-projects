import math

def insert(lines):
    print("ID:", math.floor(len(lines)/3))
    lines.append(input("Name: ") + " \n")
    lines.append(input("Age: ") + " \n")
    lines.append(input("School year: ") + " \n")
    return lines

def delete(lines):
    id = input("ID: ")
    for i in range(math.floor(len(lines)/3)):
        if i == id:
            lines.pop(i*3)
            lines.pop(i*3)
            lines.pop(i*3)
    return lines

def select(lines):
    id = input("ID: ")
    for i in range(math.floor(len(lines)/3)):
        if i == id:
            print("Name:", lines[id*3].strip(" \n") + ", age:", lines[id*3+1].strip(" \n") + ", school year:", lines[id*3+2].strip(" \n"))
        else:
            print("ID not found")

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

try:
    file = open("data.txt","r+")
except:
    file = open("data.txt","w+")
lines = file.readlines()
while True:
    for i in range(math.floor(len(lines)/3)):
        if len(lines) > 2:
            print("\n" + str(i) + " - name:", lines[i*3].strip(" \n") + ", age:", lines[i*3+1].strip(" \n") + ", school year:", lines[i*3+2].strip(" \n") + "\n")
    function = input("Function (insert, i; delete, d; select, s; replace, r; exit, e): ")
    if function.strip(" ") == "i":
        lines = insert(lines)
        file.writelines(lines)
    elif function.strip(" ") == "d":
        lines = delete(lines)
        file.writelines(lines)
    elif function.strip(" ") == "s":
        select(lines)
    elif function.strip(" ") == "r":
        lines = replace(lines)
        file.writelines(lines)
    elif function.strip(" ") == "e":
        break
file.close()