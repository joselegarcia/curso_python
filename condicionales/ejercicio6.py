renta= float(input('cual es tu renta?'))
if renta<10000:
    print('tu tipo impositivo es de 5%')
elif 10000<renta<20000:
        tax=5
elif 20000<renta<35000:
       tax=15 
elif 35000<renta<60000:
       tax=30
elif renta>60000:
        tax=45
print('tu tipo impositivo es '+str(tax)+'%')
