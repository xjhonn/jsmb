import jsmb

con = jsmb.jsmb('00.000.000.00', 'usuario', 'password')

# listar
list = con.list('Compartida')
for i in range(len(list)):
    print(list[i].filename)

# subir archivo a carpeta remota
con.upload('Compartida', 'nuevo.txt', 'tes/nuevo.txt')

# subir archivo a carpeta remota
con.download('Compartida', 'ubicacion/archivoremoto.txt',
             'dondedescargar/nuevo.txt')

# eliminar archivo
con.delete('Compartida', 'archivoaeliminar.txt')

# crear carpeta
con.mkdir('Compartida', 'jhon/j/nuevo.txt')
