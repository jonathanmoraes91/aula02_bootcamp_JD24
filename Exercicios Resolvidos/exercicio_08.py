# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

print("Vamos calcular a potência de um número?")
decisão_do_usuário = str(input("Digite sim, caso deseje continuar!"))

if decisão_do_usuário == 'sim':
    numero_01 = float(input("Inserir número base: "))
    expoente_01 = float(input("Inserir expoente: "))

    resultado = numero_01 ** expoente_01

    print("A potência do número base",numero_01,"elevado pelo expoente",expoente_01,"é:",resultado)

else:
    print("ok, vamos deixar para uma outra hora, otário!")