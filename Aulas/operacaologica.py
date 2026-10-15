#and -> retorna True quando ambas condicoes forem verdades
#or -> retorna true se pelo menos uma das condiçoes forem verdadeiras
#not -> Inverte o valor logico. Se a condicao for true, se torna False. vice - versa

temp = int(input('digite a temperatura: '))
umidade = int(input('Digite a umdade do ar em %: '))
if temp > 25 and umidade > 60:
    print('O dia está quente e umido')
else: print(' O dia não está quente e umido')
print()

