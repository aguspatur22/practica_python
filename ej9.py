from string import ascii_letters
ingreso = input("Ingrese una palabra o frase: ").replace(" ","")

es = True
for x in ingreso:
    if (x in ascii_letters):
        cant = ingreso.count(x)
        if cant>1:
            es = False

if es:
    print("Es un heterograma!")
else:
    print("No es un heterograma")