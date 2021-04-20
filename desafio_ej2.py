import csv
from collections import Counter

archivo = open("appstore_games.csv", "r")
csvreader = csv.reader(archivo, delimiter=',')

encabezado = next(csvreader)

juegos = {}

for i in csvreader:
    if i[6] not in ('' or ' '):
        juegos[i[0]] = int(i[6])

max = Counter(juegos).most_common(10)
print('Los 10 juegos con mas User rating: ')
print(dict(max))

archivo.close()