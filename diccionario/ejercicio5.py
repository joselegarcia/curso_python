d={'Matematicas':6,'Fisica':4, 'Quimica':5}
total=0
for i,j in d.items():
    print( i,' tiene ',j,' creditos.')
    total+= j
print('el total de creditos ',total)