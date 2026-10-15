compras =["ovos", 'leite','farinha']
print(compras)
compras.append('café')
print(compras)
compras.append('cereal')
print(compras)
compras.remove('ovos')
print(compras)
compras.remove('cereal')
print(compras)
compras.append('yorgute')
print(compras)
compras.remove('café')
print(compras)
print()

pessoas = ['Alexandre', "Cauã","Murilo",'Samuel','Bruno']
pessoas.insert(1,'Anônimo')
pessoas.pop(0)
pessoas.pop(-1)
print()

numeros = [1,2,3,4,5,]
numeros.append(6)
numeros.pop(0)
numeros.pop(-1)
numeros.append(7)
numeros.pop(0)
#1,2,3,4,5,6
#2,3,4,5,6
#2,3,4,5
#2,3,4,5,7
#3,4,5,7
print(numeros)
print()

a = [1, 2, 3]
b = a
c = a[:]
b.append(4)
c.append(99)
print(a)
print(c)
print()

convidados = ["Ana", "Bruno", "Carla", "Diego"]
nome = input("Seu nome: ")

if nome in convidados: #in -> busca o nome dentro da lista.
    print("Pode entrar.")
else:
    print("Nao pode entrar.")

#min -> retorna o menor numero da lista
#max -> retorna o maior numero da lista
#pop(0) -> remove por index
#pop() -> remove o ultimo
#in -> busca o nome dentro da lista
#lower -> força em minusculo