# Faça um programa que leia as 3 notas de um aluno e calcule a média aritimética deste aluno

nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))
nota3 = float(input("Entre com a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aprovado, parabéns!")
    print("A média do aluno foi {:.1f}".format(media))
else:
    print("Reprovado!")
    print("A média do aluno foi {:.1f}".format(media))
