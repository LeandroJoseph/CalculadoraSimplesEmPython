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