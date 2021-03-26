nombres = """
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
nombres = nombres.replace("\'","")

#al haber nombres repetidos, no se puede usar un 
#diccionario, ya que las claves deben ser unicas!

lista_nom = nombres.replace(",","").split()
lista_n1 = notas1.replace(",","").split()
lista_n2 = notas2.replace(",","").split()

#se convierten explicitamente las listas de notas a int
indice = 0
for i in lista_n1:
    lista_n1[indice] = int(i)
    indice+=1

indice = 0
for i in lista_n2:
    lista_n2[indice] = int(i)
    indice+=1

#se crea una lista de tuplas con nombres y suma de notas
lista_suma = [a + b for a, b in zip(lista_n1,lista_n2)]

l_final=list(zip(lista_nom,lista_suma))

#Calculo del promedio
total = sum(lista_suma) 
prom = total / len(l_final)

#Recorro una vez mas la lista de tuplas para informar
#los que obtuvieron menos que el promedio

print()
print("Alumnos con puntaje menor que el promedio (prom={:.5f}): ".format(prom))
print()

for i in l_final:
    if i[1] < prom:  #indice arranca en 0, es decir en la posicion 1 esta el valor de la nota total a comparar
        print(i)
