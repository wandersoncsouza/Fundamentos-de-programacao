print('EXERCICIO 012')
print('Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias')
tempo = int(input())
ano = tempo // 365
mes = (tempo - ano*365)//30
dia = int((tempo % 30)/2)
print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dia))