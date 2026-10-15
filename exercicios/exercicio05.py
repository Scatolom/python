peso = float(input('Peso(kg): '))
if peso == 1:
    print('Frete de R$:10,00')
elif peso > 1 and peso <= 5:
    print('Frete de R$:20,00')
else:
    print('Frete de R$:35,00')
print()

opcao = input('Digite uma opção: ')
if opcao == '1':
    print('Você escolheu Saldo')
elif opcao == '2':
    print('Você escolheu Extrato')
elif opcao == '3':
    print('Você escolheu Sair')
else: print('Opção invalida!')