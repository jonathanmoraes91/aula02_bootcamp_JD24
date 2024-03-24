# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

import math

print("Vamos converter a temperatura de Celsius para Fahrenheint?")
decisão_do_usuário = str(input("Digite sim, caso deseje continuar!"))

if decisão_do_usuário == 'sim':
    raio_do_circulo = float(input("Digite o raio do círculo: "))
    area_do_circulo = math.pi * raio_do_circulo ** 2

    print(f"A área do círculo é: {area_do_circulo:.2f}")

else:
    print("ok, vamos deixar para uma outra hora, otário!")