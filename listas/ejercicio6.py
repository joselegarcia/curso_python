asg= ('M,F,Q,H,L')
notas =[]
for i in range(5):
    notas1=str(input('cual es tu nota?'))
notas.extend(notas1)
if notas>4:
    print('aprobado')





subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
passed = []
for subject in subjects:
    score = float(input("¿Qué nota has sacado en " + subject + "?"))
    if score >= 5:
        passed.append(subject)
for subject in passed:
    subjects.remove(subject)
print("Tienes que repetir " + str(subjects))