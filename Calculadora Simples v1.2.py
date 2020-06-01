def print_menu():       ## Design de menu
    print ("\tBem vindo!\n")
    print (" Calculadora Simples - 1.0\n")
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
  
while loop:          ## While loop vai continuar até que seja = False
  print_menu()    ## Apresenta o menu
  operacao = int(input("Digite a operação desejada: "))

  if operacao == 1:
    print ("\nOpção 1 foi selecionada\n")
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    print("O resultado da soma é:" ,a+b)
    print("\n")
    
  elif operacao == 2:
    print ("\nOpção 2 foi selecionada\n")
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    print("O resultado da subtração é:" ,a-b)
    print("\n")
    
  elif operacao == 3:
    print ("\nOpção 3 foi selecionada\n")
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    print("O resultado da multiplicação é:" ,a*b)
    print("\n")
    
  elif operacao == 4:
    print ("\nOpção 4 foi selecionada\n")
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    print("O resultado da divisão é:" ,a/b)
    print("\n")
    
  elif operacao == 5:
    loop=False
    print ("\nAté logo!\n")
    break

  else:
    print("\nOpção inválida. Entre com uma opção válida para prosseguir...\n")
