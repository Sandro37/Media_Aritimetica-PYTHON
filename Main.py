notas = []
quantidadeAlunos = int(input("Entre com a quantidade de Alunos: "))
soma = 0
aux = 0
while aux < quantidadeAlunos:
    notas.append(float(input("Entre com A nota do aluno {}:".format(aux + 1))))
    soma += notas[aux]
    aux +=1

media = soma/quantidadeAlunos

print("A media ficou {:.2f}".format(media))