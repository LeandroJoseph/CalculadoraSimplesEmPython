from Soma import executar_soma
from Subtracao import executar_sub
from Multiplicacao import executar_mult
from Divisao import executar_div
from Exponencial import executar_exp
from Radiciacao import executar_rad

while True: #True para o loop ser controlado internamente
    print("\n" + "="*20)
    print("1- Adição")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão")
    print("5- Exponencial")
    print("6- Radiciação")
    print("0- Sair")
    print("="*20)

    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        resultado = executar_soma()
        print(f"\nSeu resultado é: {resultado:f}")
        
    elif opcao == 2:
        resultado = executar_sub()
        print(f"\nSeu resultado é: {resultado:.2f}")
    
    elif opcao == 3:
        resultado = executar_mult()
        print(f"\nSeu resultado é: {resultado:.2f}")
    
    elif opcao == 4:
        resultado = executar_div()
        print(f"\nSeu resultado é: {resultado}")

    elif opcao == 5:
        resultado = executar_exp()
        print(f"\nSeu resultado é: {resultado:.2f}")

    elif opcao == 6:
        resultado = executar_rad()
        print(f"\nSeu resultado é: {resultado:.2f}")

    elif opcao == 0:
        print("Encerrando programa...")
        break # Sai do loop e termina
    
    else:
        print("Opção inválida!")
        continue # Volta para o início do menu

    
    # Pergunta crucial após a operação
    #.lower garante que meu input virá em minusculo de qualquer maneira

    while True:
        continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
        if continuar == 'n':
            print("Encerrando programa...")
            exit() # Fecha o programa completamente
        elif continuar == 's':
            break # Sai deste laço interno e volta para o menu principal
        else:
            print("Opção inválida! Digite apenas 's' ou 'n'.")
    

# O main apenas recebe o valor pronto e exibe

#Lembrar sempre de chamar como função. Ex: "resultado=função()"
# resultado = executar_soma()

# print(f"--- RESULTADO FINAL: {resultado} ---")