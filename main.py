import math
import os
from discreto import *
from continuo import *

def main():
    archivo: str = input("Escribe el nombre del archivo: ")
    archivo = archivo + ".txt"

    if not os.path.exists(archivo):
        print("El archivo no existe")
        return

    eleccion: int = int(input(f"El archivo {archivo} es de tipo discreto (1) o continuo (2)?: "))
    if eleccion == 1:
        main_discreto(archivo)
    elif eleccion == 2:
        main_continuo()
    else: 
        print("No es válido")


if __name__ == '__main__':
    main()