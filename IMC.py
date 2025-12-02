
print("-=" * 20)
print(" CALCULADORA DE IMC ".center(40))
print("-=" * 20)

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura ** 2)

print(f"> Seu IMC atual é: {imc:.2f}")

if imc < 18.5:
    print("Você esta abaixo do peso!")
elif 18.5 <= imc < 25:
    print("Seu peso é o ideal. Parabéns!")
elif 25 <= imc < 30:
    print("ATENÇÃO! Você esta com SOBREPESO.")
elif 30 <= imc < 40:
    print("CUIDADO! Você esta com risco de OBESIDADE.")
else:
    print("PERIGO! Você esta com OBESIDADE MÓRBIDA.")
