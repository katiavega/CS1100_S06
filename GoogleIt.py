s = "    soy un hacker de CS1100    "
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.strip(" ")) #borrar espacios en blanco de los extremos
print("\t"+ s) #tab
print("\n\n"+ s)#salto de linea
print('{:100}'.format(s)) #alinear izq
print('{:^100}'.format(s))#alinear centro
print('{:>100}'.format(s)) #alinear derecha

#extra: tabular tabla.
for i in range(3,13):
    print("{:3d} {:4d} {:5d}".format(i, i*i, i*i*i))
