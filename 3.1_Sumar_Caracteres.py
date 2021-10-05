numero = input('ingrese un numero entero positivo: ')

while not numero.isnumeric() or int(numero)<1:
    numero = input('Ingreso invalidp. Ingrese un numero entero positivo: ')

numero = int(numero)
while numero >= 10:

    numero = sum(int(digito) for digito in str(numero))

print(numero)