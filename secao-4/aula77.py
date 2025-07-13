# Perguntas e Respostas

perguntas = [
    {
        'Pergunta': 'Qual o valor de "x", sendo x = 2 + 2?',
        'Alternativas': [0, 2, 4, 22],
        'Correta': 'c'
    },

    {
        'Pergunta': 'Qual o valor de "x", sendo x = (5 * 4) + (7 * 6)?',
        'Alternativas': [20, 42, 62, 840],
        'Correta': 'c'
    },

    {
        'Pergunta': 'Qual o conjunto solução de "x", sendo x = log₀.₅(3x-1) > log₀.₂₅(3)?',
        'Alternativas': ['S = { x ∈ R | 1/3 < x < (√3 - 1)/3 }', 'S = { x ∈ R | x < 1/3 ou x > (√3 - 1)/3 }', 'S = { x ∈ R | 1/3 ≤ x ≤ (√3 - 1)/3 }', 'S = { x ∈ R | x > (√3 - 1)/3 }'],
        'Correta': 'a'
    }
]

alternativa_letra = ['a', 'b', 'c', 'd']
acertos = 0

print('Bem-vindo ao jogo de perguntas e respostas de matemática!')

for pergunta in range(len(perguntas)):
    print('')
    print(f'1- {perguntas[pergunta]['Pergunta']}')
    for alternativa in range(len(perguntas[pergunta]['Alternativas'])):
        print(f'{alternativa_letra[alternativa]}) {perguntas[pergunta]['Alternativas'][alternativa]}')

    print('')
    while True:
        resposta = input('Resposta: ')
        if not resposta.isalpha():
            print('A resposta deve conter apenas a letra da alternativa!')
        elif len(resposta) > 1:
            print('Digite apenas uma letra!')
        else:
            if resposta not in alternativa_letra:
                print('Digite uma alternativa existente!')
            else:
                break
    
    if resposta == perguntas[pergunta]['Correta'][0]:
        print('Resposta correta!')
        print('Parabéns!') 

        acertos += 1
    else:
        print('Resposta incorreta!') 
        print('Não foi dessa vez!') 

print('Questionário finalizado!')
print(f'Você obteve {acertos}/{len(perguntas)}')

if (acertos / len(perguntas)) == 1:
    print('Parabéns! Você gabaritou o questionário!')
elif (acertos / len(perguntas)) >= 0.5:
    print('Muito bom! Você quase gabaritou o questionário!')
elif (acertos / len(perguntas)) == 0:
    print('Você fracassou completamente! Estude os conteúdos e tente novamente!')
else:
    print('Você pode melhorar! Reveja os conteúdos e tente novamente!')



