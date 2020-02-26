#CEDERJ - SÃO FIDELIS - FUNDAMENTOS DE PROGRAMAÇÃO
#WANDERSON C. SOUZA
print('Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro).')
print('Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.')
nome = str(input())
salario = float(input())
vendas = float(input())
comissao = vendas * 0.15
saltot = salario + comissao
print('TOTAL = R$ {:.2f}'.format(saltot))