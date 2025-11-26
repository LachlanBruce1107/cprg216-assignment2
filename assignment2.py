from gpa_functions import *

students = dict()

choice = 'y'
while choice == 'y' or choice == 'yes':
    option = show_menu()
    match option:
        case 1:
            run_search(students)
        case 2:
            run_edit(students)
        case 3:
            run_add(students)
        case 4:
            run_remove(students)
    
    choice = input("Would you like to continue(y/yes), or exit the program(n/no)? \n")