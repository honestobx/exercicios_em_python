# Faça um programa que leia as 3 notas de um aluno e calcule a média aritmética deste aluno.

nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))
nota3 = float(input("Entre com a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print("A média do aluno foi {:.1f}".format(media))