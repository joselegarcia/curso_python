inv= float(input('cuanto quieres invertir?'))
interes= float(input('que interes?'))
años= int(input('numero de años?'))
for i in  range(años):
    inv += inv*interes/100 #es el  interes compuesto
    print('cantidad tras ', i+1, 'años', inv)