import csv

archivo = open("appstore_games.csv", "r")
csvreader = csv.reader(archivo, delimiter=',')

encabezado = next(csvreader)

print('Nombre de juegos gratuitos en espanol: ')
for i in csvreader:
    if ((i[7]) == '0') and ('ES' in i[12]):
        print(i[2])

archivo.close()