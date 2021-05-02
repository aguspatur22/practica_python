import PySimpleGUI as sg

def build():
    """
    Construye la ventana del menú del juego
    """
    layout = [[sg.Button('Video Games Sales', size=(50, 2), key="-GAMES-",pad=(50,10))],
         [sg.Button('2021 Billionaires', size=(50, 2), key="-BILLIONAIRES-",pad=(50,0))],
         [sg.Button('Salir', size=(50, 2), key="-SALIR-", pad=(50,20))]]

    window = sg.Window('Actividad de Teoria',layout)

    return window
