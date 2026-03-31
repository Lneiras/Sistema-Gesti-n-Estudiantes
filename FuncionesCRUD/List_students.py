# Con esta función listaremos los estudiantes

from Otrasfunciones.aspectos_visuales import *

def List_students(Student_list):
    Loading()

    if not Student_list: 
        print(f"{Azul}\nEmpty student list{Reset}")
        return
    
    clean_screen()
    Students = "Students list"
    print(f"{edgeL}")
    print(f"{Verde}{Students:^{widthL}}{Reset}")
    print(f"{edgeL}")
    print(f"{'ID':<6} | {'Student':<16} | {'Age':<6} | {'Course':<16} | {'Status':<9}")
    print(f"{edgeL}")

    for i in Student_list:
        print(f"{i['Id']:<6} | {i['student']:<16} | {i['age']:<6} | {i['course']:<16} | {i['status']:<9}")

