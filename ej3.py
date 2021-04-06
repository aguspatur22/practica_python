import string

texto = "hola como andas bien todo tranquilo yo y vos que arbol hermoso ola ira piedra"

letra = input("Ingrese una letra: ")
if letra not in string.ascii_letters:
    print("No ingreso una letra. Intente nuevamente: ")

palabras = []
data = texto.split()
for i in data:
    if i[0] == letra:
        palabras.append(i)

print(palabras) 