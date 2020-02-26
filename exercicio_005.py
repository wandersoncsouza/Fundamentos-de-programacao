print('EXERCICIO 005')
print('Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe \npor hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas \ncasas decimais.')
nunfunc = int(input())
hrtrab = int(input())
vlrhora= float(input())
sal = hrtrab * vlrhora
print('NUMBER = {} \nSALARY = U$ {:.2f}'.format(nunfunc, sal))
