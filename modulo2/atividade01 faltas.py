nomeAluno = input('qual o nome do aluno')
nota1 = float(input('qual a primeira nota'))
nota2 = float(input('qual a segunda nota'))
faltas = int(input('quantas faltas teve'))

media = (nota1 + nota2)/2

if media<7 or faltas>3:
    print('o desenpenho da media foi' ,media, ' e a quantidade de faltas foi' ,faltas, 'o aluno foi reprovado')
else:
    print('aprovado') 

