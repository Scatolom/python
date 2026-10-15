#while - repete o bloco de codigo, enquanto a condição for True.
# situacao = True
# while situacao == True:
#     print("codigo se repete")

# saldo = 100000
# while saldo > 0:
#     valorsaque = int(input("Valor do saque: "))
#     saldo = (saldo - valorsaque)
#     print(saldo)
# print()

soma = 0
num = int(input("digite um numero: "))
while num != 0:
    soma = (soma + num)
    num = int(input("digite um numero: "))
print('Soma: ', soma)