# A rede Casas Bahia lança todo mês de dezembro a promoção 
# “Compre hoje e passe um ano pagando”, que consiste em parcelar 
# a compra em 12x sem juros. Faça um programa que receba um valor 
# de uma compra e mostre o valor das prestações

valor = float(input("Entre com o valor a ser dividido em 12x: "))

parcela = valor/12

print("Valor de R${:.2f} será pago em 12 parcelas de R${:.2f}".format(valor,parcela))