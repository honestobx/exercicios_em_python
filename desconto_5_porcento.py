# O app iFood está oferecendo 5% de desconto para todos os usuários. 
# Faça um programa que possa receber um valor de um pedido e que 
# escreva o desconto e o valor a pagar.

valor = float(input("Entre com valor do pedido: "))

desconto = valor * 0.05
valor = valor - desconto

print("Desconto de R${:.1f}".format(desconto))
print("Valor a pagar com desconto de 5% é R${:.1f}".format(valor))