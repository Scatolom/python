#For -> percorre uma lista/array, e a cada volta, a variavel recebe um elemento
#for elemento in lista: repete para cada lista
precos = [19.90, 5.50, 42.00]
for preco in precos:
    print('R$', preco)

notas = [7.5, 4.0, 9.0, 5.5]
for nota in notas:
    if nota >= 6:
        print('Aprovado')
    else:
        print('Reprovado')
print()

carrinho = [12.50, 30.00, 7.50]
valor = 0
for soma in carrinho:
    valor += soma # == total = (valor + soma)
print('R$', valor)
