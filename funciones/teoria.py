def saludo():
    print('Hola')
    return

saludo()#siempre con parantesis aunque no tenga parametros

#parametros=variables
#argumentos=definir la variable 
def saludo(nombre):
    print('Hola ',nombre)
    return
saludo('jose')
saludo('alf')

#arg.posicionales:asgnar parametros por orden
def saludo(nombre,apellido):
    print('Hola ',nombre, apellido)
    return
saludo('jose','garcia')

def saludo(nombre,apellido):
    print('Hola ',nombre, apellido)
    return
saludo('garcia','jose')

#arg.por_nombre
def saludo(nombre,apellido):
    print('Hola ',nombre, apellido)
    return#se pone sin nada para mostrar que hay acaba la funcion 
saludo(apellido='garcia',nombre='jose')

#funcion;area trinagulo
def area_tringulo(base,altura):
    return (base * altura) / 2
print(area_tringulo(5,20))
print(area_tringulo(3,6))

 #VALORxDEFECTO:
def area_tringulo(base,altura=10): #si no introduces altura, cogeria 10,si pones altura toma ese valor sino toma 10(por defecto)
    return (base * altura) / 2
print(area_tringulo(3))

#cuanod hay un arterisco(*)delante de un parametro es que es indefinido

def menu(*platos): #platos es una secuencia de parametros, los va agrupar en una tupla
    print(platos)
    return
menu('pan','agua','pastel')

def menu(*platos):
    for i in platos:
        print(i)
    return
menu('pan','agua','pastel')

#****ambito de los paramentros,variables de la funcion 

#ambito local:dentro funcion
#amb_global:fuera de la funcion, desde global puedo acceder a local(viceversa NO)
def menu(*platos):
    for i in platos:
        print(i)
    return
menu('pan','agua','pastel')
print(platos)
#es error pq platos no esta definido, tendrias definirla en el return

nombre='jose'
def menu(*platos):
    print('menu de ',nombre)
    for i in platos:
        print(i)
    return
menu('pan','agua','pastel')

nombre='jose'
def menu(*platos):
    nombre='alf'
    print('menu de ',nombre)
    for i in platos:
        print(i)
    return
menu('pan','agua','pastel')

nombre='jose'
def menu(*platos):
    nombre='alf'
    print('menu de ',nombre)
    for i in platos:
        print(i)
    return
menu('pan','agua','pastel')
print(nombre)

menu=['pan','agua'] #listas es mutable, al hacer un cambio dentro d ela funcion se refleja fuera
def añade_plato(menu,plato):
    """
    Funcion para añadir un plato a la funcion menu.
    Parametros:
        -menu:es una lista con platos
        -plato:es una cadena xcon un plato 
    """
    menu.append(plato)
    return
añade_plato(menu,'pastel')
print(menu)

help(añade_plato)#te devuelve el doctring=es un comentrario especial para funciones: """
#hay que ejecutarlo en terminal

help(sum)#docstrng de la funcion suma 