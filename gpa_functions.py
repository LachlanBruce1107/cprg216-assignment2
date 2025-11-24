def show_menu():
    print("What would you like to do today?")
    print("-Find a student? enter 1")
    print("-Edit a student's info using student ID? enter 2")
    print("-Add a new student? enter 3")
    print("-Remove a student? enter 4")
    return input()

def add(students,id,name,gpa,semester):
    #adds a student to the dictionary, with their id being the key, and the value being another dictionary with atributes of the student within
    students[id] = {"name":name,"gpa":gpa,"semester":semester}

def remove(students,id):
    #removes a students dictionary entry, using their id to locate their info
    students.pop(id)

def edit_name(students,id,new_name):
    #edits a students name within the nested dictoinary
    students[id]["name"] = new_name

def search():
    pass

def run_search():
    pass

def run_edit(students):
    id = input("Enter the id of the student. Enter -1 to return to the previous menu\n")
    if id == -1:
        return
    else:
        new_name = input("Enter the new name of the student\n")
        edit_name(students,id,new_name)
        print("Student name modified for the student with id",id)
        print("Student's new name is",new_name)
        


def run_add(students):
    choice = "y"
    while choice == "y" or choice == "yes":
        print("Enter id of the student, followed by the student's information.")
        id = input("id:\n")
        name = input("name:\n")
        gpa = input("gpa:\n")
        semester = input("semester:\n")
        add(students,id,name,gpa,semester)
        print("Student added")
        print(id,name,gpa,semester, sep="\t")
        choice = input("Do you want to add a new student?y(yes)/n(no)\n").lower()


def run_remove(students):
    choice = "y"
    while choice == "y" or choice == "yes":
        print("Enter id of the student that you want to remove from the students' registry.")
        id = input("id:\n")
        remove(students, id)
        print("Student removed")
        choice = input("Do you want to remove more students?y(yes)/n(no)\n").lower()