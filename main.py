from Otrasfunciones.Otras_funciones import *
from FuncionesCRUD.Register_students import *
from FuncionesCRUD.List_students import *
from FuncionesCRUD.Search_student import *
from FuncionesCRUD.Update_student import *
from FuncionesCRUD.Remove_student import *



Student_list = []


def main():
    clean_screen()
    print(f"{Azul}\nWelcome to the student management system{Reset}\n")

    counter = ""

    while counter != 1:

        option = menu()

        if option == "1":
            student = Register_student(Student_list)
            Student_list.append(student)
            Coming_back()

        elif option == "2":
            List_students(Student_list)
            Coming_back()
        
        elif option == "3":
            Search_student(Student_list)
            Coming_back()
        
        elif option == "4":
            Update_student(Student_list)
            Coming_back()

        elif option == "5":
            Remove_student(Student_list)
            Coming_back()
        
        elif option == "6":
            Leaving()
            exit()
            counter = 1
        
        else:
            print(f"{Rojo}Error, invalid option, please try again.{Reset}")


main()