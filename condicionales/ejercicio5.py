nombre= str(input('cual es tu nombre?'))
sexo= str(input('cual es tu sexo: (M o H)?'))
if sexo == 'M':
    if nombre.lower() < 'm':
        grupo = 'A'
    else:
        grupo = 'B'
else:
    if nombre.lower() < 'n':
        grupo = 'A'
    else:
        grupo = 'B'
print ('tu grupo es '+grupo)
#otra forma de crear la condicional, esta vez sin anidar.
name = input("¿Cómo te llamas? ")
gender = input("¿Cuál es tu sexo (M o H)? ")
if (gender == "M" and name.lower() < 'm') or (gender == "H" and name.lower() > 'n'):
    group = "A"
else:
    group = "B"
print("Tu grupo es " + group)