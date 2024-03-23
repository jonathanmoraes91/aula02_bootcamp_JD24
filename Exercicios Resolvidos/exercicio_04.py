# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

print("Vamos fazer uma conta de divisão de números inteiros?")
print("Digite sim, caso deseje continuar!")
decisão_do_usuário = str(input())

if decisão_do_usuário == 'sim':
    numero_01 = int(input("Inserir um número inteiro: "))
    numero_02 = int(input("Inserir outro número inteiro: "))
    
    resultado = numero_01 // numero_02

    print("O resultado da divisão inteira é:", resultado)

else:
    print("ok, vamos deixar para uma outra hora, otário!")