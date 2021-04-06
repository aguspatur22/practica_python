nom1 = """
'Agustin',
 'Alan',
 'Andrés',
 'Ariadna',
 'Bautista',
 'CAROLINA',
 'CESAR',
 'David',
 'Diego',
 'Dolores',
 'DYLAN',
 'ELIANA',
 'Emanuel',
 'Fabián',
 'Facundo',
 'Facundo',
 'FEDERICO',
 'FEDERICO',
 'GONZALO',
 'Gregorio',
 'Ignacio',
 'Jonathan',
 'Jonathan',
 'Jorge',
 'JOSE',
 'JUAN',
 'Juan',
 'Juan',
 'Julian',
 'Julieta',
 'LAUTARO',
 'Leonel',
 'LUIS',
 'Luis',
 'Marcos',
 'María',
 'MATEO',
 'Matias',
 'Nicolás',
 'NICOLÁS',
 'Noelia',
 'Pablo',
 'Priscila',
 'TOMAS',
 'Tomás',
 'Ulises',
 'Yanina'
"""

nom2 = """
'Agustin',
 'AGUSTIN',
 'Agustín',
 'Ailen',
 'Alfredo',
 'Amalia',
 'Ariana',
 'Bautista',
 'Braian',
 'Carla',
 'CESAR',
 'Daniel',
 'Diego',
 'ELIANA',
 'Facundo',
 'Facundo',
 'Facundo',
 'Facundo',
 'Federico',
 'Federico',
 'Flavia',
 'Francisco',
 'Germán',
 'Guido',
 'GUSTAVO',
 'Hilario',
 'Ignacio',
 'IVAN',
 'Jimmy',
 'Joaquín',
 'Jose',
 'Josue',
 'JUAN',
 'Juan',
 'Laura',
 'LAURA',
 'Lautaro',
 'Lautaro',
 'Ludmila',
 'Marcos',
 'Marcos',
 'MARIANELA',
 'MARTIN',
 'MATEO',
 'Mateo',
 'Matias',
 'MAURO',
 'Maximiliano',
 'NESTOR',
 'Nicolas',
 'Pedro',
 'Ramiro',
 'Sofía',
 'Tobias',
 'Tomás',
 'Tomás',
 'Ulises',
 'Yanina'
"""

notas1 = """
81,
 60,
 72,
 24,
 15,
 91,
 12,
 70,
 29,
 42,
 16,
 3,
 35,
 67,
 10,
 57,
 11,
 69,
 12,
 77,
 13,
 86,
 48,
 65,
 51,
 41,
 87,
 43,
 10,
 87,
 91,
 15,
 44,
 85,
 73,
 37,
 42,
 95,
 18,
 7,
 74,
 60,
 9,
 65,
 93,
 63,
 74
"""

notas2 = """
30,
 95,
 28,
 84,
 84,
 43,
 66,
 51,
 4,
 11,
 58,
 10,
 13,
 34,
 96,
 71,
 86,
 37,
 64,
 13,
 8,
 87,
 14,
 14,
 49,
 27,
 55,
 69,
 77,
 59,
 57,
 40,
 96,
 24,
 30,
 73,
 95,
 19,
 47,
 15,
 31,
 39,
 15,
 74,
 33,
 57,
 10
"""
nom1 = nom1.replace("\'","")
lista_nom1 = nom1.replace(",","").split()
nom2 = nom2.replace("\'","")
lista_nom2 = nom2.replace(",","").split()
\

#Genero la lista por comprension con los nombres
#que se encuentran en ambas estructuras
lista = [x for x in lista_nom1 if x in lista_nom2]

print(f'Alumnos en comun: {lista}')

lista_notas1 = notas1.replace(",","").split()
lista_notas2 = notas2.replace(",","").split()

#se convierten explicitamente las listas de notas a int
indice = 0
for i in lista_notas1:
    lista_notas1[indice] = int(i)
    indice+=1

indice = 0
for i in lista_notas2:
    lista_notas2[indice] = int(i)
    indice+=1

#lista de suma de notas
lista_suma = [a + b for a, b in zip(lista_notas1,lista_notas2)]

#formato = "{:4} {:20} {:5} {:5} {:5}"  #se define una vez y luego se puede usar todas las veces que quieras!!!
print(f"{''}{'Nombre':>10}{'Eval1':>15}{'Eval2':>20}{'Total':>25}") #aca si a los str le ponias comillas dobles te tiraba error pq era como q estabas cerrando el string!! 
indice = 0
for i in lista_nom1:
    print(f"{indice}{i:>10}{lista_notas1[indice]:>15}{lista_notas2[indice]:>20}{lista_suma[indice]:>25}")
    indice+=1