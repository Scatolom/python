temperaturas = [22, 31, 27, 35, 19]
maior =0
for elemento in temperaturas:
    if  elemento > maior:
        maior = elemento
print(maior)
print()

#len -> tamanho, ou seja, retorna a quantidade de elementos ou de caracteres deum objeto
palavras = ["sol", "computador", "casa", "python", "janela"] # array
contador =  0 #variavel de controle
for palavra in palavras: # o for analiza a array
    if len(palavra) > 5: # o for vai analizando cada item da array e checando se possui mais de 5 caracteres
        contador += 1 # se o if for true, ele vai somar +1 no valor de contador
print(contador) # imprime o resultado
print()

nomes = ["Ana", "Bruno", "Carla", "Ana"]
sim = 0 
for nome in nomes:
    if nome == 'Ana':
        sim += 1
        print(sim)
print()

nomes1 = ["Lucas", "Pedro", "Julia", "Marcos"]
for procura in nomes1:
   if procura == "Pedro":
    print('Achei o Pedro')
print()

nomes = ["João", "Maria", "João", "Paula"]
contador1 = 0
for joao in nomes:
   if joao == 'João':
    contador1 += 1
    print(contador1)