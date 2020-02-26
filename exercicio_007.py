#CEDERJ - SÃO FIDELIS - FUNDAMENTOS DE PROGRAMAÇÃO
#WANDERSON C. SOUZA
print('EXERCICIO 007')
print('Faça um programa que calcule e mostre o volume de uma esfera sendo fornecido o valor de seu raio (R).')
print('A fórmula para calcular o volume é: (4/3) * pi * R3. Considere (atribua) para pi o valor 3.14159.')
pi = 3.14159
raio = float(input())
esfera = (4/3.0) * pi * (raio**3)
print('VOLUME = {:.3f}'.format(esfera))