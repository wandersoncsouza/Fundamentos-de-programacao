print('EXERCICIO 002')
print('A fórmula para calcular a área de uma circunferência é: area=π . raio2. Considerando para este problema que π=3.14159:\n- Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.')
raio = float(input('Informe o ráio:'))
n = 3.14159
area = (raio ** 2) * n
print('A={:.4f}'.format(area))
