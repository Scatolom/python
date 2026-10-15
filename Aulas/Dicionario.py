#Dicionario
#chave e valor

aluno = { "nome": "Ana", "idade": 20, 
           "curso": "Python", 
           "EstadoCivil": "Solteira"
         , "Altura": 1.70  }

print(aluno["nome"])

aluno["nome"] = "Lucas" #alterar valor de uma chave.

del aluno["Altura"] #deletar uma chave do dicionario.

for chave, valor in aluno.items():
    print(chave, "->", valor)


print(aluno)

