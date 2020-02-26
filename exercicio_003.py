print('EXERCICIO 003')
print('Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, calcule a média do aluno,\nsabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.')
A, B, C = float(input()), float(input()), float(input())
media = (A*2 + B*3 + C*5)/10
print("MEDIA = {:.1f}".format(media))
