'''In this function we will search for students; we will use it in the update and delete functions.'''

from Otrasfunciones.aspectos_visuales import *
from Otrasfunciones.Otras_funciones import *

def search_ID(Student_list, searched_ID):
        
    for Num_id in Student_list:
        if str(Num_id["Id"]) == searched_ID:
            return Num_id        
    return None

def search_name(Student_list, searched_name):
        
    for name in Student_list:
        if name["student"] == searched_name:
            return name        
    return None

def Search_student(Student_list):
    clean_screen()

    if not Student_list:
        print(f"{Azul}\nEmpty student list{Reset}")
        return

    counter = ""
    while counter != 1 :
        
        print("Select a search option\n")

        search_option = search_menu()

        if search_option == "1":  #Search by name

            clean_screen()
            counter1 = ""
            while counter1 != 1 : 

                searched_name = input("\nEnter the customer's name (or type 'exit' to return to the menu): ").strip().lower()

                if searched_name == "exit": 
                    print(f"\n{Amarillo}Search canceled{Reset}")
                    return

                name = search_name(Student_list, searched_name)

                if name:
                    print(f"{edgeC}")
                    print(f"{Verde}Student found!{Reset}")
                    print(f"{edgeC}")
                    print(f"ID:  {name['Id']}")
                    print(f"Student:  {name['student']}")
                    print(f"Age: {name['age']}")
                    print(f"Course: {name['course']}, Status: {name['status']}")
                    print(f"{edgeC}")                
                    return name
                else:
                    print(f"\n{Rojo}Error: The client name '{searched_name}' does not exist {Reset}")
                    print("Try again...\n")
                    continue
        
        if search_option == "2":  #Search by ID
            clean_screen()
            counter2 = ""
            while counter2 != 1: 

                searched_ID = input("\nEnter the customer ID (or type 'exit' to return to the menu): ").strip().lower()

                if searched_ID == "exit": 
                    print(f"\n{Amarillo}Search canceled{Reset}")
                    return 

                Num_id = search_ID(Student_list, searched_ID)

                if Num_id:
                    print(f"{edgeC}")
                    print(f"{Verde}Student found!{Reset}")
                    print(f"{edgeC}")
                    print(f"ID:  {Num_id['Id']}")
                    print(f"Student:  {Num_id['student']}")
                    print(f"Age: {Num_id['age']}")
                    print(f"Course: {Num_id['course']}, Status {Num_id['status']}")
                    print(f"{edgeC}")                
                    return Num_id
                else:
                    print(f"\n{Rojo}Error: The client ID '{searched_ID}' does not exist.{Reset}")
                    print("Try again...\n")
                    continue
        
        if search_option == "3": #Exit
            clean_screen()
            print(f"\n{Amarillo}Search canceled{Reset}")
            counter = 1