def calculadora(x, y, operacao):
    if operacao == '+' :
        return soma(x,y)
    elif operacao == '-':
        return subtracao(x,y)
    elif operacao == '*':
        return multiplicacao(x,y)
    else:
        return divisao(x,y)

def soma(x,y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    return "Não é possível dividir por 0!"