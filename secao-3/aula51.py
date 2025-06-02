# Introdução ao desempacotamento

lista_nomes = ['Vinicius', 'Eduardo', 'Gustavo']
nome1, nome2, nome3 = lista_nomes
print(nome1)
print(nome2)
print(nome3)

# Uma variável '_', por convenção, representa uma variável que não vai ser usada no código
nome4, *_ = ['Vini', 'Edu', 'Batata']
print(nome4, _)


