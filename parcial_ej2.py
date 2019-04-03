monedas=[5,2,1]
cantidad = int(input('introduce tus un numero entero'))
cambio= [0,0,0] #nueva lista 
#como lo haria un humano, empezar dando de 5, hasta sea menor, empzar a dar de 2, hasta que sea menor,...
for i in range(len(monedas)):#empieza a tomar valores, el primero las monedas de 5
    while cantidad>=monedas[i]:
        cantidad -= monedas[i]
        cambio[i]+= 1
print('el numero minimo de monedas es'+ sum(cambio))
#para que lo muestre por pantalla
for i in range(len(monedas)):
    print(cambio[i], 'monedas de '+ monedas[i], '€')
     

coins = [5, 2, 1]
change = [0, 0, 0]
amount = int(input("Introduce una cantidad entera de euros: "))
print('Para sumar', amount, '€ se necesitan ', end='')
for i in range(len(coins)):
    while amount >= coins[i]:
        amount -= coins[i]
        change[i] += 1
print(sum(change), 'monedas:')
for i in range(len(coins)):
    print(change[i], 'monedas de ', coins[i], '€')