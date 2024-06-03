from collections import Counter
import math
from discreto import *

def main():
    eleccion: int = int(input("Prefieres usar el método discreto (1) o el continuo (2)?: "))
    if eleccion == 1:
        main_discreto()
    elif eleccion == 2:
        main_continuo()
    else: 
        print("No es válido")


if __name__ == '__main__':
    main()