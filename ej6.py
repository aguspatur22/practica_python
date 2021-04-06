frase="""Si trabajás mucho CON computadoras, eventualmente
encontrarás que te gustaría automatizar alguna tarea.
Por ejemplo, podrías desear realizar una búsqueda y
reemplazo en un gran número DE archivos de texto, o 
renombrar y reorganizar un montón de archivos con
fotos de una manera compleja. Tal vez quieras escribir
alguna pequeña base de datos personalizada, o una
aplicación especializada con interfaz gráfica, o UN
juego simple."""

lista = frase.lower().split()
lista_nueva = []

for x in lista:
    if x not in lista_nueva:
        lista_nueva.append(x)

print(lista_nueva)

#en realidad se podria hacer mas facil con set()
#pero todavia no lo vimos eso 