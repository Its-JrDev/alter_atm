import os
from functions import authentication, menu_options
os.system('clear')

print('\nBienvenido/a la red de cajeros de TechBank Riwi Digital')
if authentication():
    balance = 1000
    try:
        n_operations = int(input('Ingrese el número de operaciones a realizar: '))
        if n_operations <= 0:
            print('Error: Escoja un número positivo.')
    except ValueError:
        print('Error, debe ingresar un número.')
    for i in range(n_operations):
        balance, salir = menu_options(balance)
        
        if salir:
            break
    print('\nGracias por usar el cajero automático')
