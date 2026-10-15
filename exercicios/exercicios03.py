#EXERCICIO 01

pessoa01 = input('idade: ')
pessoa02 = input('idade: ')
if(pessoa01 == pessoa02):
    print('As idades são iguais')
else: print('As idade não são iguais')
print()

#EXERCICIO 02

num01 = input('digite um numero: ')
num02 = input('digite um numero: ')
if(num01 == num02):
    print('Numeros iguais')
else: print('Numeros não iguais')
print()

#EXERCICIO 03

altura01 = input("digite sua altura(cm): ")
altura02 = input("digite sua altura(cm): ")
if(altura01 > altura02):
    print ('altura01 é mais alto')
else:print ('altura02 é mais alto')
if(altura01 == altura02):
    print('alturas iguais')
print()

#EXERCICIO 04

nota = float(input("nota alcançada: "))
nota_min = float(input("nota minima: "))
if(nota >= nota_min):
    print("Você passou!!!")
else: print('Você não passou =(')
print()

#EXERCICIOS 05

horas = int(input("digite o numero de horas estudadas: "))
horas_min = int(input("digite o numero minimo de horas à serem estudadas: "))
if (horas >= horas_min):
    print("Estudou o necessario")
else: print('Não estudou o necessario')