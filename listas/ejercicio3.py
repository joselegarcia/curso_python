asignaturas= ['Estadistica', 'Programacion', 'Historia']
notas=[]
for i in asignaturas:
     c=float(input('que has sacado en '+i+'?:'))
notas.append(c)
for a in range(len(asignaturas)):
    print('he sacado en '+asignaturas[a]+ 'un '+notas[i])


subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
passed = []
for subject in subjects:
    score = float(input("¿Qué nota has sacado en " + subject + "?"))
    if score >= 5:
        passed.append(subject)
for subject in passed:
    subjects.remove(subject)
print("Tienes que repetir " + str(subjects))