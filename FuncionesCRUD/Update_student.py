from Otrasfunciones.aspectos_visuales import *
from FuncionesCRUD.Search_student import *


def Update_student(Student_list):
    clean_screen()

    if not Student_list:
        print(f"{Azul}\nEmpty student list{Reset}")
        return
    
    counter = ""
    while counter != 1:

        student = Search_student(Student_list)

        if student is None:
            print(f"{Amarillo}update canceled{Reset}") 
            return
        
        update_option = update_menu()

        if update_option == "1":  
            print("Select the new course\n")
            counter1 = ""
            while counter1 != 1:
                New_course = Courses_menu()

                '''En este caso se realiza la creación de un diccionario con los planes disponibles para que fuese más sencillo realizar.
                Las validaciones y, si es necesario, posteriormente realizar cambios en estos planes o agregar más sin tener que reestructurar mucho del código.'''
                Courses = {
                            "1": "Web Development",
                            "2": "English",
                            "3": "Life skills"
                        }

                if New_course in Courses:
                    selection = Courses[New_course]
                    
                    if student["course"] == selection:
                        print(f"\n{Rojo}Error: The user is already registered in the '{selection}' course.{Reset}")
                        print("Please select a different plan or type 'exit'.")
                        continue 
                    
                    student["Plan"] = selection
                    print(f"\n{Verde}Student successfully registered for the course {selection}!{Reset}")
                    Coming_back()
                    counter1 = 1

            else:
                print(f"{Rojo}Invalid option, please try again.{Reset}")
                continue

        elif update_option == "2": #Actualizar Estado plan
                Loading()
                salir = ""
                while salir != 1:
                        
                    status = student["status"]

                    if status.lower() == "active":
                        student["status"] = "inactive"
                        salir = 1
                    
                    elif status.lower() == "inactive":
                        student["status"] = "active"
                        salir = 1
                        
                print(f"\n{Verde}Change in the status of the course successfully completed{Reset}")

        elif update_option== "3": #salir
            print(f"\n{Amarillo}Upgrade operation cancelled.{Reset}")
            break
        
        else:
            print(f"\n{Rojo}Error: Invalid option, please try again{Reset}")
            continue