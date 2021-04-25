# Escreva um programa para ler o número total de eleitores de um município, 
# o número de votos brancos, nulos e válidos. Calcular e escrever o percentual 
# que cada um representa em relação ao total de eleitores.

total = int(input("Entre com número total de eleitores: "))

brancos = int(input("Entre com número de votos brancos: "))
nulos = int(input("Entre com número de votos nulos: "))
validos = int(input("Entre com número de votos válidos: "))

brancos = float(brancos/100)*total
nulos   = float(nulos/100)*total
validos = float(validos/100)*total

print("Porcentagem em votos válidos {:.1f}% ".format(validos))
print("Porcentagem em votos nulos {:.1f}% ".format(nulos))
print("Porcentagem em votos brancos {:.1f}% ".format(brancos))
print("De um total de {} eleitores".format(total))