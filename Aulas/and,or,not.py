preco = float(input('preço: '))
estoque = int(input('quantidade: '))
if preco > 50 and estoque > 10:
    print('Você tem um desconto!')
else: print('sem desconto disponível')
print()

idade = int(input('Sua idade: '))
estudante = input('Voce é estudante: (s/n)')
if idade < 18 or estudante == 's':
    print('Meia entrada')
else: print('inteira')
print()

tem_ingresso = False
if not tem_ingresso:
    print('compre seu ingresso!')