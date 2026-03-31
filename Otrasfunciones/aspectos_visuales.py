#En este archivo se definen funciones que ayudan con el aspecto visual para el programa

#Los colores se definen aquí para no agregarlos en cada archivo de manera individual

#colores
Rojo = "\033[31m"
Verde = "\033[32m"
Amarillo = "\033[33m"
Azul = "\033[34m"
Magenta = "\033[35m"
Cian = "\033[36m"
Blanco = "\033[37m"
Reset = "\033[0m"

'''Esta parte es para determinar valores para agregar cuadros a la parte visual del usuario
sin tener que agregar esa información en cada archivo de manera individual'''


#Dimensiones
widthC = 35    #recuadros cortos
edgeC = "─" * widthC
widthM = 55    #recuadros medianos
edgeM = "─" * widthM
widthL = 80   #recuadros largos
edgeL = "─" * widthL
widthP = 100  #Recuadros para la lista
edgeP = "─" * widthP

import os

#This function cleans the screen so the user sees a cleaner program.
def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


#These features add a visual touch for the user

def Coming_back(): #volviendo
    input(f"\n{Amarillo}Press Enter to return to the menu{Reset}")
    import time
    print("\nComing back...")
    time.sleep(1.5)  # Pausa de 1.5 segundos
    clean_screen()

def Adding(): #agregando
    clean_screen()
    import time
    print("\nAdding...")
    time.sleep(1.5)  # Pausa de 1.5 segundos
    clean_screen()
    print(f"{Verde}\nInformación agregada con éxito{Reset}")

def Loading(): #cargando
    clean_screen()
    import time
    print("\nLoading...")
    time.sleep(1.5)  # Pausa de 1.5 segundos
    clean_screen()

def Leaving(): #saliendo
    clean_screen()
    import time
    print("\nLeaving...")
    time.sleep(1.5)  # Pausa de 1.5 segundos
    clean_screen()