# 23: Calculadora Simples

try:
    numero_01 = float(input("Digite o primeiro número: "))
    numero_02 = float(input("Digite o segundo número: "))
    operador = input("Digite um dos seguintes operadores (+, -, *, /): ")

    if operador == '+':
        resultado = numero_01 + numero_02
    elif operador == '-':
        resultado = numero_01 - numero_02
    elif operador == '*':
        resultado = numero_01 * numero_02
    elif operador == '/' and numero_02 != 0:
        resultado = numero_01 / numero_02
    else:
        print("Operador inválido ou divisão por zero!")
    print(f"Segue resultado: {resultado}")
except ValueError:
    print("Erro: Entrada inválida. Ceritifique-se de inserir números para o cálculo!")
except NameError:
    print("Não foi possível concluir o cálculo!")
    