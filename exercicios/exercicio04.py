usuario = input('Digite seu email: ')
senha = input('Digite sua senha: ')
if usuario == 'aluno' and senha == '1234':
    print('Login realizado')
else: print('Usuário ou senha incorretos')
print()

dia = input('Digite o dia da semana: ')
if dia == 'sabado' or dia =='domingo':
    print('Final de semana')
else:print('Dia útil')
print()

bateria_carregada = False
if not bateria_carregada:
    print('conecte o carregador')
else: print('bateria OK')