# Todos os produtos do site AliExpress são apresentados em dólar. 
# Faça o programa que calcule o valor correspondente em Reais, 
# a partir da cotação do dólar do dia fornecido pelo usuário

cota = float(input("Entre com a cotação do dólar do dia de hoje: "))
valor = float(input("Entre com valor doláres do produto: "))

valor = valor * cota

print("Valor do produto em reais será de R${:.1f}".format(valor))