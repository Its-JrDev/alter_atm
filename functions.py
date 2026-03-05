def authentication():
    #user = 'Rrraaaaaamiro
    user = 'admin'
    pin = 4545
    count_auth = 4

    while count_auth > 0:
        print('\nIniciar sesión')
        auth_user = input('\nIngrese su Usuario: ')
        try:
            auth_pin = int(input('Ingrese su PIN: '))
        except ValueError:
            count_auth -= 1
            print(f'Error: El PIN debe ser numérico. Le quedan {count_auth} intentos.')
            continue
        if auth_user == user and auth_pin == pin:
            print("\nInicio de sesión exitoso.")
            return True
        else:
            count_auth -= 1
            print(f'\nError: Usuario o PIN incorrectos. Le quedan {count_auth} intentos.')
    print("\nCuenta bloqueada. Demasiados intentos fallidos.")
    return False

def menu_options(balance):
    print('\nSistema Transaccional Bancario')
    print('\n1. Consultar saldo', '\n2. Retirar dinero', '\n3. Depositar dinero', '\n4. Salir')
    
    try:
        option = int(input('\nIngrese una de las opciones 1-4: '))
    except ValueError:
        print('Error: Debe ingresar un número.')
        return balance, False
    
    if option == 1:
        print(f'Balance: {balance}')
    
    elif option == 2:
        while True:
            try:
                retiro = float(input('\nIngrese el monto a retirar: '))
                if retiro > balance:
                    print('Fondos insuficientes.')
                elif retiro <= 0:
                    print('Monto inválido.')
                else:
                    balance -= retiro
                    print(f'Usted ha retirado {retiro} pesos con éxito.')
                    print(f'Su nuevo balance es: {balance}')
                    break
            except ValueError:
                print('Error: El monto debe ser un número.')
    elif option == 3:
        while True:
            try:
                deposito = float(input('Ingrese el monto a depositar: '))
                if deposito > 0:
                    balance += deposito
                    print(f'Usted ha depositado {deposito} pesos con éxito.')
                    print(f'Su nuevo balance es: {balance}')
                    break                    
                else: 
                    print('Monto inválido, inténtelo de nuevo')
            except ValueError:
                print('Error: El monto debe ser un número.')
                
    elif option == 4:
        print('\nUsted ha salido del sistema bancario con éxito')
        return balance, True
    
    else:
        print('Opción inválida. Inténtelo de nuevo.')
    
    return balance, False