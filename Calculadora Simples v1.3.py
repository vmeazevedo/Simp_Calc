def print_menu():       ## Design de menu
    print ("\n\tBem vindo!\n")
    print (" Calculadora Simples - 1.3\n")
    print("\n As operações que você pode fazer nessa calculadora são:\n")
    print ("1. Soma")
    print ("2. Subtração")
    print ("3. Divisão")
    print ("4. Multiplicação")
    print ("5. Sair\n")

#Variaveis
soma = 1
subtração = 2
divisão = 3
multiplicação = 4
sair = 5

loop=True      
  
print_menu()    ## Apresenta o menu

while loop:          ## While loop vai continuar até que seja = False
    operacao = int(input("Digite a operação desejada: "))

    if operacao == 1:
      print ("\nOpção 1 foi selecionada.\n")
      a = float(input("Digite o primeiro número, caso for um número decimal utilize ponto ao invés de vírgula: "))
      b = float(input("Digite o segundo número, caso for um número decimal utilize ponto ao invés de vírgula: "))
      print("O resultado da soma é: {:.2f}.".format(a+b))
      print("\n")
      quest = str(input('Deseja realizar mais alguma operação? S ou N: ')).lower()
      if quest == 's':
        print('\n\n\n')
        print('='*60)
        print('='*60)
        print_menu()
      else:
        print('Obrigado por usar a aplicação. Até logo!')
        break
      
    elif operacao == 2:
      print ("\nOpção 2 foi selecionada.\n")
      a = float(input("Digite o primeiro número, caso for um número decimal utilize ponto ao invés de vírgula: "))
      b = float(input("Digite o segundo número, caso for um número decimal utilize ponto ao invés de vírgula: "))
      print("O resultado da subtração é: {:.2f}.".format(a-b))
      print("\n")
      quest = str(input('Deseja realizar mais alguma operação? S ou N: ')).lower()
      if quest == 's':
        print('\n\n\n')
        print('='*60)
        print('='*60)
        print_menu()
      else:
        print('Obrigado por usar a aplicação. Até logo!')
        break
      
    elif operacao == 3:
      print ("\nOpção 3 foi selecionada.\n")
      a = float(input("Digite o primeiro número, caso for um número decimal utilize ponto ao invés de vírgula: "))
      b = float(input("Digite o segundo número, caso for um número decimal utilize ponto ao invés de vírgula: "))
      print("O resultado da multiplicação é: {:.2f}.".format(a/b))
      print("\n")
      quest = str(input('Deseja realizar mais alguma operação? S ou N: ')).lower()
      if quest == 's':
        print('\n\n\n')
        print('='*60)
        print('='*60)
        print_menu()
      else:
        print('Obrigado por usar a aplicação. Até logo!')
        break
      
    elif operacao == 4:
      print ("\nOpção 4 foi selecionada.\n")
      a = float(input("Digite o primeiro número, caso for um número decimal utilize ponto ao invés de vírgula: "))
      b = float(input("Digite o segundo número, caso for um número decimal utilize ponto ao invés de vírgula: "))
      print("O resultado da divisão é: {:.2f}.".format(a*b))
      print("\n")
      quest = str(input('Deseja realizar mais alguma operação? S ou N: ')).lower()
      if quest == 's':
        print('\n\n\n')
        print('='*60)
        print('='*60)
        print_menu()
      else:
        print('Obrigado por usar a aplicação. Até logo!')
        break
      
    elif operacao == 5:
      loop=False
      print ("\nAté logo!\n")
      break

    else:
      print("\nOpção inválida. Entre com uma opção válida para prosseguir...\n")
