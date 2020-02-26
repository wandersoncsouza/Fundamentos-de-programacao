print('EXERCICIO 011')
print('Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.')
total = int(input())
horas = total //3600
minutos = (total - horas*3600)//60
segundos = (total % 60)
print('{}:{}:{}'.format(horas, minutos, segundos))