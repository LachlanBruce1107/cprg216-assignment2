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

def remove():
    pass

def edit_name():
    pass

def search():
    pass

def run_search():
    pass

def run_edit():
    pass

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


def run_remove():
    pass