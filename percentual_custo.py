# Um Programa que receba o preço de custo de um produto
# e mostre o valor de venda. Sabe-se que será acrescido um
# um percentual informado pelo usuário sobre o preço de custo.

valorCusto = float(input("Entre com valor de custo do produto: "))

valorPercentual = float(input("Entre com valor com a porcentagem de acréscimo: "))

valorPercentual = valorCusto * valorPercentual
valorVenda = valorCusto + valorPercentual

print("O valor de venda do produto será R${:.2f}".format(valorVenda))