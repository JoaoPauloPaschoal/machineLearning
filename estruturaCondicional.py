n1 = float(input("Qual a nota do aluno? "))
n2 = float(input("Qual a segunda nota do aluno? "))
media = (n1 + n2) / 2

if media >= 6:
    print("Aluno aprovado! ")
else:
    print("Aluno reprovado! ")

print("Nota final recebida: " ,media)