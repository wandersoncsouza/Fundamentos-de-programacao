print('EXERCICIO 008')
print('Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).')
print('O arquivo de entrada contém dois valores: um valor inteiro X representando a distância total percorrida (em Km), \ne um valor real Y representando o total de combustível gasto, com um dígito após o ponto decimal.')
km = int(input())
lt = float(input())
consumo = km / lt
print('{:.3f} km/l'.format(consumo))