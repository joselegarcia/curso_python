meses= {'01':'enero', '02':'febrero', '03':'marzo', '04':'abril'}
fecha={input('introduce un fecha en formato dd/mm/aa')}
fecha = fecha.split('/')#va a partir por donde este el simblolo
print(fecha[0],'de ', meses.get(fecha[1]), 'de ' ,fecha[2])