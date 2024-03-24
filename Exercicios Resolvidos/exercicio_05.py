# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

print("Vamos calcula o quadrado de um número inteiro?")
print("Digite sim, caso deseje continuar!")
decisão_do_usuário = str(input())

if decisão_do_usuário == 'sim':
    numero_01 = int(input("Inserir um número inteiro: "))
    
    resultado = numero_01 ** 2

    print("O quadrado do número ", numero_01, "é:", resultado)

else:
    print("ok, vamos deixar para uma outra hora, otário!")