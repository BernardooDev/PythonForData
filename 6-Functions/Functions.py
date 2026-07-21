print(10 + 20)
print(30 + 50)
print(100 + 200)

# Com função:
def somar(a, b):
    return a + b

print(somar(10, 20))
print(somar(30, 50))
print(somar(100, 200))

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

imc = calcular_imc(70, 1.75)

print(imc)