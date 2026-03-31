'''This document will contain the additional functions and menus of the program.'''
from Otrasfunciones.aspectos_visuales import *

def menu():

    print(f"{Magenta}┌{edgeC}┐")
    print(f"│{Blanco}{"1. Register new students":<{widthC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"2. List students":<{widthC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"3. Search student":<{widthC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"4. Update student":<{widthC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"5. Remove student":<{widthC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"6. Exit":<{widthC}}{Reset}{Magenta}│")
    print(f"└{edgeC}┘{Reset}")

    
    option = input(f"{Blanco}\nEnter the desired option: ")
    return option

def exit():
    clean_screen()
    Exit_text = "Thank you for using the student management system"
    print(f"{Magenta}┌{edgeP}┐")
    print(f"│{Blanco}{Exit_text:^{widthP}}{Reset}{Magenta}│")
    print(f"└{edgeP}┘{Reset}")


def Courses_menu():

    print(f"{Magenta}┌{edgeC}┐")
    print(f"│{Blanco}{"1. Web Development":<{widthC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"2. English":<{widthC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"3. Life skills":<{widthC}}{Reset}{Magenta}│")
    print(f"└{edgeC}┘{Reset}")

    
    course_option = input(f"{Blanco}\nSelect the course: ")
    return course_option

def search_menu():
    print(f"{Magenta}┌{edgeC}┐")
    print(f"│{Blanco}{"1. Search by name":<{widthC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"2. Search by ID":<{widthC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"3. Exit":<{widthC}}{Reset}{Magenta}│")
    print(f"└{edgeC}┘{Reset}")

    search_option = input(f"{Blanco}\nEnter the desired option: ")
    return search_option

def update_menu():
    print(f"{Magenta}┌{edgeC}┐")
    print(f"│{Blanco}{"1. Update course":<{widthC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"2. Update status":<{widthC}}{Reset}{Magenta}│")
    print(f"│{Blanco}{"3. Exit":<{widthC}}{Reset}{Magenta}│")
    print(f"└{edgeC}┘{Reset}")

    update_option = input(f"{Blanco}\nEnter the desired option: ")
    return update_option