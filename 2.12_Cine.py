edad = int(input('Bienvenido al CineUNIMET\n Ingrese su edad para determinar el costo de su boleto: '))

if(edad<4):
    print('Tu entradas en GRATIS!!')
elif(edad>= 4 and edad<=18):
    print('El precio de tu entrada es de $10')
elif(edad>18):
    print('EL precio de tu entrada es de $14')