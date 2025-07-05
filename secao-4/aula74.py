# Closure functions e funções que retornam outras funções

def saudacao(texto):
    def saudar_nome(nome):
        return f'{texto}, {nome}!'
    return saudar_nome

bom_dia = saudacao('Bom dia')
boa_tarde = saudacao('Boa tarde')
boa_noite = saudacao('Boa noite')

lista_nomes = ['Vinicius', 'Eduardo', 'Gustavo']
for nome in lista_nomes:
    print(bom_dia(nome))
    print(boa_tarde(nome))
    print(boa_noite(nome))