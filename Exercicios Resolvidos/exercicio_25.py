# 25: Conversão de Tipo com Validação

entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []

try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print(f"Lista de inteiros: {numeros_int}")
except ValueError:
    print("Erro: Certifique-se de que todos os elementos são números inteiros válidos!")