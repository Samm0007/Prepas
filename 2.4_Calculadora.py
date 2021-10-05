print('Bienvenido a la calculadora, ingresa por teclado que tipo de operacion quieres realizar. \n1.-Suma\n2.-Resta\n3.-Multiplicacion\n4.-Division\n5.-Potencia\n6.-Modulo\n7.-Compara <,>,=\n8.-Valor absoluto')
repetir = 'Y'
while(repetir == 'Y'):

    seleccion = int(input('Ingrese la opcion con el numero que lo representa:'))

    while(seleccion<1 or seleccion>8):
        seleccion = int(input('Seleccion invalida. Ingrese la opcion con el numero que lo representa: '))


    if(seleccion!=8):
        if (seleccion == 1):
            print('Haz elegido Suma.')
            primerValor=float(input('Ingresa tu primer valor: '))
            segundoValor=float(input('Ingresa tu segundo valor: '))
            print(f'El resultado es {primerValor+segundoValor}')
        elif(seleccion == 2):
            print('Haz elegido Resta.')
            primerValor=float(input('Ingresa tu primer valor: '))
            segundoValor=float(input('Ingresa tu segundo valor: '))
            print(f'El resultado es {primerValor-segundoValor}')
        elif(seleccion == 3):
            print('Haz elegido Multiplicacion.')
            primerValor=float(input('Ingresa tu primer valor: '))
            segundoValor=float(input('Ingresa tu segundo valor: '))
            print(f'El resultado es {primerValor*segundoValor}')
        elif(seleccion == 4):
            print('Haz elegido Division.')
            primerValor=float(input('Ingresa tu primer valor: '))
            segundoValor=float(input('Ingresa tu segundo valor: '))
            while(segundoValor==0):
                segundoValor=float(input('La division entre 0 no esta definida, ingrese otro valor'))
            print(f'El resultado es {primerValor/segundoValor}')
        elif(seleccion == 5):
            print('Haz elegido Potencia.')
            primerValor=float(input('Ingresa tu primer valor: '))
            segundoValor=float(input('Ingresa tu segundo valor: '))
            print(f'El resultado es {pow(primerValor,segundoValor)}')
        elif(seleccion == 6):
            print('Haz elegido Modulo.')
            primerValor=float(input('Ingresa tu primer valor: '))
            segundoValor=float(input('Ingresa tu segundo valor: '))
            print(f'El resultado es {primerValor-segundoValor}')
        elif(seleccion == 7):
            print('Haz elegido Comparar <,>,=.')
            primerValor=float(input('Ingresa tu primer valor: '))
            segundoValor=float(input('Ingresa tu segundo valor: '))
            if(primerValor < segundoValor):
                print(f'{primerValor}<{segundoValor}')
            elif (primerValor > segundoValor):
                print(f'{primerValor}>{segundoValor}')
            elif (primerValor == segundoValor):
                print(f'{primerValor}={segundoValor}')
    else:
        print('Haz elegido Valor absoluto.')
        primerValor=float(input('Ingresa el valor: '))
        print(f'El resultado es {abs(primerValor)}')

    repetir = input('Quieres realizar otra operacion ? (Y): ')