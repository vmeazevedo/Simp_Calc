print("\tBem vindo!\n\n Calculadora Simples - 1.0\n\n As operações que você pode fazer nessa calculadora são:\n \n 1-Soma\n 2-Subtração\n 3-Divisão\n 4-Multiplicação\n\n")

soma = 1
subtração = 2
divisão = 3
multiplicação =4

operacao = int(input("Digite a operação desejada: "))
print("\n")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
print("\n")

if operacao == 1:
    print("O resultado da soma é:" ,a+b)
    pass

if operacao == 2:
    print("O resultado da subtração é:" ,a-b)
    pass

if operacao == 3:
    print("O resultado da divisão é:" ,a/b)
    pass

if operacao == 4:
    print("O resultado da multiplicação é:" ,a*b)
    pass
