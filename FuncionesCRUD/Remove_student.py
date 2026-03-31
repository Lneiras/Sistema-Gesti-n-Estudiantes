from Otrasfunciones.aspectos_visuales import *
from FuncionesCRUD.Search_student import *

#Search_student(Student_list)


def Remove_student(Student_list):
    clean_screen()

    if not Student_list:
        print(f"{Azul}\nEmpty student list{Reset}")
        return
    
    student = Search_student(Student_list)

    if student is None:
        print(f"{Amarillo}Elimination canceled{Reset}") 
        return
    
    counter = ""

    while counter != 1:

        Delete = input(f"\n{Amarillo}Please confirm if you wish to delete this client (Yes/No):  {Reset}").strip().lower()

        if Delete == "yes":
            Student_list.remove(student)
            print(f"{Rojo}student removed{Reset}")
            counter = 1
        
        elif Delete == "no":
            print(f"\n{Amarillo}Elimination canceled{Reset}")
            counter = 1

        else:
            print(f"\n{Rojo}Invalid option, please try again{Reset}")
            continue