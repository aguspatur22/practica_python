frase = input("Ingrese una frase: ")
palabra = input("Ingrese una palabra a contar en la frase: ").lower()

lista = frase.replace(",","").lower().split()

cant = 0
for i in lista:
    if i == palabra:
        cant+=1

print(cant)