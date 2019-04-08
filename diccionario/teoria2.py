l1=[1,2,3]
l2=l1
print(l2)
l2.remove(2)#l1 tmabien se vera afectada, copia por referencia

l1=[1,2,3]
l2=list(l1)
print(l2)
l2.remove(2)
print(l2)
print(l1)#al elimanar en l2, l1 no se ve afectada, copia por valor



d1={1:'a',2:'b',3:'c'}
d2=dict(d1)
print(d2)
del d2(2)
print(d1)
#lo mismo pero para diccionarios
