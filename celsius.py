# Faça um programa que leia uma temperatura em graus Celsius e apresente-a
# convertida em graus Fahrenheit. A fórmula de conversão é: F = (9 * C + 160) / 5,
# na qual F é a temperatura em Fahrenheit e C é a temperatura em Celsius
# Observação: Para testar se a sua resposta está correta saiba que 100ºC = 212F

c = float(input("Entre com número em Celsius: "))

fah = (9 * c + 160) / 5
print("Numero em celsius é {:.1f}F em fahrenheit.".format(fah))