fruteria={'manzanas':0.80, 'platanos':1.35, 'peras':0.85, 'naranjas':0.70}
fruta=input('que fruta quieres?:')
kg= float(input('cuantos kilos quieres?:'))
if fruta in fruteria:
    print('el precio es',fruteria.get(fruta)*kg)
else:
    print('no tenemos', fruta)
