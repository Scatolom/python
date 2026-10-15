senha = 1234
a = int(input('Digite a senha: '))
while a != senha:
    a = int(input('Digite a senha: '))
if a == senha:
    print('Senha correta')
print()

sim = 5
b = int(input('adivinhe um numero entre 1 e 20: '))
while b != sim:
    b = int(input('Errado, tente novamente: '))
if b == sim:
    print('Você acertou!!!')
print()
