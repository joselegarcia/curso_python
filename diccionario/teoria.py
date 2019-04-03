#elemtos no ordenados, accedes a los elemntos atraves de su clave
#lo que sta primero es la clave, lo segundo es el valor asociado 
alf={'nombre':'alf', 'despacho':'218','email':'asalber@ceu.es'}
pablo={'nombre':'pablo','despacho':'684'}
profes ={'06236':alf, '07465':pablo}#meto un diccionario dentro de otro diccionario
#para acceder d.get(clave, valor)
alf.get('universidad','CEu')#no existe clave universidad, muestra ceu
alf.get('despacho','CEU')#la clave despacho tine valor asociado
profes['06236']['email']#para acceder se usan corchetes
profes.get('06236').get('email')

#operaciones que no  modifican:
for clave in alf.keys():#.keys genera las listas de las claves
    print(clave)

for clave in alf.values():
    print(clave)

for clave, valor in alf.items():#de devuelve los pares en un tupla
    print(clave, ':', valor )


