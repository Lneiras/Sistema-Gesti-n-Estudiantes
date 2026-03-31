# Con esta función agregaremos estudiantes nuevos

from Otrasfunciones.aspectos_visuales import *
from Otrasfunciones.Otras_funciones import *
import random


def Register_student(Student_list): 

    clean_screen() 

    Register= "Register a new student"
    print(f"{edgeM}")
    print(f"{Verde}{Register:^{widthM}}{Reset}")
    print(f"{edgeM}")
    
    counter = ""

    while counter != 1:

        name = input(f"{Cian}\nEnter the student's name: {Reset}").strip().lower()

        if not name.replace(" ","").isalpha() or len(name) == 0:
            print(f"{Rojo}Error: The name must contain only letters{Reset}")
            continue

        '''With 'replace' we remove spaces from the name, while 'isalpha'
        verifies that they are letters and not other types of characters.
        With 'len' we ensure that it is not empty.'''
# Here we confirm if the user exists; if so, it sends an error message so we can register another one.
        exists = any(i['student'].lower() == name for i in Student_list)
        if exists:
            clean_screen()
            print(f"{Rojo}Error: this student already exists.{Reset}")
            continue 
            
        else:
            print(f"{Verde}\nName added successfully{Reset}")
            counter = 1
    
    counter2 = ""
    while counter2 != 1:

        Age = input(f"{Cian}\nEnter the student's age: {Reset}").strip()
        
        if not Age.isdigit() or int(Age)<= 0: # Here we confirm that it is a positive number
            print(f"{Rojo}Error: The age must contain only positive numbers.{Reset}")
            continue

        else:
            print(f"{Verde}\nAge added successfully{Reset}")
            counter2 = 1

    counter3 = ""
    while counter3 != 1:

        course_option = Courses_menu() 
# Here we select the course in which the student is registered and it is automatically left in active status.
        if course_option== "1":
            print(f"\n{Verde}The student was successfully enrolled in the web development course\n{Reset}")
            course = "Web Development"
            status = ("Active")
            counter3 = 1
        elif course_option == "2": 
            print(f"\n{Verde}The student was successfully enrolled in the english course\n{Reset}")
            course = "English"
            status = ("Active")
            counter3 = 1
        elif course_option == "3": 
            print(f"\n{Verde}The student was successfully enrolled in the life skills course\n{Reset}")
            course = "Life skills"
            status = ("Active")
            counter3 = 1
        else:
            print(f"{Rojo}Invalid option, please try again.{Reset}")
            continue

    while True: #cIn this function we create a unique ID using 'random'. In this while loop we ensure that the generated number is not repeated.
        Num_id = random.randint(1000, 9999)
        if Num_id not in Student_list:
            break

    return {"Id": int(Num_id), "student": name, "age": int(Age), "course": course, "status": status}


