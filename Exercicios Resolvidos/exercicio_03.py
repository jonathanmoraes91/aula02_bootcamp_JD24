# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

print("Vamos fazer uma conta de multiplicação de números inteiros?")
print("Digite sim, caso deseje continuar")
decisão_do_usuário = str(input())

if decisão_do_usuário == 'sim':
    numero_01 = int(input("Inserir um número inteiro: "))
    numero_02 = int(input("Inserir outro número inteiro: "))
    
    resultado = numero_01 * numero_02

    print(resultado)

else:
    print("ok, vamos deixar para uma outra hora, obrigado por participar!")

