# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

print("Vamos converter a temperatura de Celsius para Fahrenheint?")
decisão_do_usuário = str(input("Digite sim, caso deseje continuar!"))

if decisão_do_usuário == 'sim':
    celsius_01 = float(input("Digite a temperatura em celsius: "))
    fahrenheint_01 = (celsius_01 *9/5) + 32

    print(f"A temperaatura de {celsius_01}ºC é igual a {fahrenheint_01}ºF")

else:
    print("ok, vamos deixar para uma outra hora, otário!")