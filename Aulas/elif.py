#if condicao 
# executa 
# elif outra condicao 
# else
# se nenhuma condicao acima for TRUE
velocidade = int(input('Velocidade do carro em km/h: '))
if velocidade <= 60:
    print('Dentro do limite')
elif velocidade > 60 and velocidade <= 80:
    print ('multa leve - passou do limite')
elif velocidade > 80 and velocidade <= 100:
    print('Multa grave - passou do limite')
else: print('Multa gravissima')
print()
