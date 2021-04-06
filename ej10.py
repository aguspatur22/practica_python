dicc = {}

for i in "AEIOULNRST":
    dicc[i] = 1

for i in "DG":
    dicc[i] = 2

for i in "BCMP":
    dicc[i] = 3

for i in "FHVWY":
    dicc[i] = 4

dicc["K"] = 5

for i in "JX":
    dicc[i] = 8

for i in "QZ":
    dicc[i] = 10

palabra = input("Ingrese una palabra: ").upper()

valor = 0
for p in palabra:
    valor+=dicc[p]

print(f"Valor: {valor}")