import math

def executar_fat():
    n1=int(input("Digite um valor:\n"))

    resultado = math.factorial(n1)

    print(f"O fatorial de {n1} é {resultado}")
    return resultado