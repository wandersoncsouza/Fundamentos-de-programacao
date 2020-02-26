print('EXERCICIO 010')
print('Joaozinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem, ao utilizar um \nautomóvel que faz 12 KM/L. Para isso, ele gostaria que você o auxiliasse através de um simples programa. Para')
print('efetuar o cálculo, deve-se fornecer o tempo gasto na viagem (em horas) e a velocidade média durante a mesma \n(em km/h). Assim, pode-se obter distância percorrida e, em seguida, calcular quantos litros seriam necessários. \nMostre o valor com 3 casas decimais após o ponto.')
time = int(input())
velocidade = int(input())
kmh = (time * velocidade)/12
print('{:.3f}'.format(kmh))
 