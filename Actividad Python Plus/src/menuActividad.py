import PySimpleGUI as sg
import csv
import json
import v_menu

sg.theme('DarkGray2')

def move(data,path):
    '''
    Transfiere los datos del parametro 'data' a un archivo JSON en la ruta recibida en 'path'
    '''
    with open(path, 'w') as arch:
        json.dump(data, arch, indent=4)


def games():
    '''
    Filtra el contenido de vgsales.csv obteniendo el nombre de dichos juegos que se produjeron para Play 2 y por Sony,
    y que tuvieron ventas GLOBALES de mas de medio millon. https://www.kaggle.com/gregorut/videogamesales
    '''
    try:
        archivo = open('../Datasets/vgsales.csv','r')
        datos = []
        for i in csv.DictReader(archivo):
            if (i["Platform"] == "PS2" and i["Publisher"] == "Sony Computer Entertainment" and float(i["Global_Sales"]) >= 0.5 ):
                datos.append(i["Name"])
        archivo.close()
        sg.popup("Archivo de analisis: videojuegos creado !")
        return datos

    except FileNotFoundError:
        sg.popup("Hubo un error! Intenta de nuevo ")


def limpiar(string):
    ''' Limpia el campo del NetWorth para quedarse solo con el valor numerico'''
    string = string.replace('B','')
    return float(string.replace('$',''))

def billionaires():
    '''
    Filtra el contenido de Billionaires.csv obteniendo el nombre de todos los billonarios de Argentina y de aquelllos de
    Estados Unidos que tienen un NetWorth que oscila entre 4 y 7 billones. https://www.kaggle.com/roysouravcu/forbes-billionaires-of-2021
    ''' 
    try:
        archivo = open('../Datasets/Billionaire.csv','r')
        csvreader = csv.DictReader(archivo)
        #Otra forma distinta de filtrar: 
        datos2 = list(map(lambda x: x["Name"] ,filter(lambda x: x["Country"] == "Argentina" or (x["Country"] == "United States" and 4.0 < limpiar(x["NetWorth"]) < 7.0),csvreader)))
        archivo.close()
        sg.popup("Archivo de analisis: Top Billionaires creado !")
        return datos2

    except FileNotFoundError:
        sg.popup("Hubo un error ")


def start():
    """
    Lanza la ejecución de la ventana del menú
    """

    window = loop()
    window.close()
    

def loop():
    """
    Loop de la ventana de menú que capta los eventos al apretar las opciones
    """

    window = v_menu.build()

    while True:
        event, values = window.read()
        
        if event == sg.WINDOW_CLOSED or event == '-SALIR-':
            break
        
        if event == "-GAMES-":
            window.hide()
            datos = games()
            move(datos,'../Analisis/vgsales.json')
            window.un_hide()
        
        if event == "-BILLIONAIRES-":
            window.hide()
            datos2 = billionaires()
            move(datos2,'../Analisis/billionaire.json')
            window.un_hide()
    
    return window

start()