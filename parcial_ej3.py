# word es una lista, si esta vacia tiene valor False, si no True
word = list(input('Introduce la palabra a adivinar: '))
failures = 0
while word and failures < 5:
    letter = input('Introduce una letra: ')
    if letter in word:
        print('Acierto')
        word.remove(letter)
    else:
        print('Fallo')
        failures += 1
if failures == 5:
    print('Perdiste')
else:
    print('Ganaste') 



word = input('Introduce la palabra a adivinar: ')
word = list(word)
solution = list('*' * len(word))
failures = 0
while any(word) and failures < 5:
    letter = input('Introduce una letra: ')
    if letter in word:
        print('Acierto')
        i = word.index(letter)
        word[i] = False
        solution[i] = letter
    else:
        print('Fallo')
        failures += 1
    print(solution)
if failures == 5:
    print('Perdiste')
else:
    print('Ganaste') 