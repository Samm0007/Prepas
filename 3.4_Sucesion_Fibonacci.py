numero = input('ingrese un numero entero positivo: ')

while not numero.isnumeric() or int(numero)<1:
    numero = input('Ingreso invalidp. Ingrese un numero entero positivo: ')

x=0
y=1
z=1

sucesion = [str(x)]

while z<= int(numero):
    sucesion.append(str(z))
    z = x+y
    x=y
    y=z

print(",".join(sucesion))