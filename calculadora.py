def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

print("=== CALCULADORA ===")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Escolha uma operação: ")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if opcao == "1":
    print("Resultado:", soma(numero1, numero2))

elif opcao == "2":
    print("Resultado:", subtracao(numero1, numero2))

elif opcao == "3":
    print("Resultado:", multiplicacao(numero1, numero2))

elif opcao == "4":
    if numero2 == 0:
        print("Não é possível dividir por zero")
    else:
        print("Resultado:", divisao(numero1, numero2))

else:
    print("Opção inválida")

print("Obrigado por usar a calculadora!")