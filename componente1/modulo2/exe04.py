def soma(x,y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    return "Não é possível dividir por 0."

while True:
    print("Qual operação você deseja realizar? \n")
    print("1: Soma\n2: Subtração\n3: Multiplicação\n4: Divisão\n0: Sair")
    opcao = int(input("Digite alguma das opções acima: "))

    if opcao == 0:
        print("Finalizando calculadora!")
        break
    
    x = int(input("Insira o primeiro valor: "))
    y = int(input("Insira o segundo valor: "))

    if opcao == 1:
        print("Resultado:", soma(x, y))
    elif opcao == 2:
        print("Resultado:", subtracao(x, y))
    elif opcao == 3:
        print("Resultado:", multiplicacao(x, y))
    elif opcao == 4:
        print("Resultado:", divisao(x, y))
    else:
        print("Informe uma operação correta!")

