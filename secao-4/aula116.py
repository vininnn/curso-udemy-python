# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho_arquivo = 'C:\\Documents\\Estudos\\Udemy\\curso-python\\secao-4\\'
caminho_arquivo += 'aula116.txt'

#arquivo = open(caminho_arquivo, 'w')
#arquivo.close()
with open(caminho_arquivo, 'w+') as arquivo: # Abre e fecha o arquivo
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0, 0)
    print(arquivo.read())

# with open(caminho_arquivo, 'r', encoding='utf-8) as arquivo: Colocar encoding caso necessário para o vscode mostrar icones UTF-8 se não aparecem
with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())
