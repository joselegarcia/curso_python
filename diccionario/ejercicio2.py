usuario={}
usuario['nombre']= input('introduce tu nombre')
usuario['edad']= input('introduce tu edad')
usuario['dirreccion']= input('introduce tu direccion')
usuario['telefono']= input('introduce tu telefono')
print(usuario.get('nombre'), 'tiene', usuario.get('edad') ,'años, vive en', usuario.get('direccion'), 'y su número de teléfono es' ,usuario.get('telefono'),'.')
