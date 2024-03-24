# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

print("Vamos calcular a média de dois números?")
print("Digite sim, caso deseje continuar!")
decisão_do_usuário = str(input())

if decisão_do_usuário == 'sim':
    numero_01 = float(input("Inserir primeiro número: "))
    numero_02 = float(input("Inserir segundo número: "))

    resultado = (numero_01 + numero_02) / 2

    print("A soma dos números",numero_01,"e",numero_02,"é:",resultado)

else:
    print("ok, vamos deixar para uma outra hora, otário!")