import math

def executar_soma():
    # A lógica de entrada e cálculo fica aqui
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    
    resultado = n1 + n2
    return resultado

def executar_sub():

    n1 = float(input("Digite o primeiro número: \n"))
    n2 = float(input("Digite o segundo número: \n"))

    resultado = n1-n2
    return resultado

def executar_mult():
    # A lógica de entrada e cálculo fica aqui
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    
    resultado = n1 * n2
    return resultado

def executar_div():
    # A lógica de entrada e cálculo fica aqui
    while True:
        try:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            
            if n2 != 0:
                resultado = n1/n2
                return (resultado)
            
            elif n2 == 0:
                print("\nERRO: Divisão por zero não permitida!")
                tentar = input("Deseja tentar outros números? (s/n): ").lower()
                if tentar == 'n':
                    return None # Sai da função e volta pro menu
                elif tentar == 's':
                    continue # Volta pro início do 'while' para pedir os números de novo
            return n1 / n2 # Se deu tudo certo, retorna o resultado e encerra a função
            
        except ValueError:
            print("Erro: Por favor, digite apenas números.")

def executar_exp():
    n1 = float(input("Digite o número: \n"))
    n2 = float(input("Digite o expoente: \n"))

    resultado = n1 ** n2
    return resultado

def executar_fat():
    n1=int(input("Digite um valor:\n"))

    resultado = math.factorial(n1)

    print(f"O fatorial de {n1} é {resultado}")
    return resultado

def executar_rad():
    
    n1 = float(input("Digite o número: "))
    n2 = float(input("Digite o indicie da raiz: "))

    resultado = (n1**(1/n2))

    return resultado