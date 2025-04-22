nome = input('Qual é o seu nome? ')
idade = input('Qual é a sua idade? ')

if (nome == '') or (idade == '') :
    print('Você deixou campos vazios!')
else :
    print(f'O seu nome é {nome}.')
    print(f'O seu nome invertido é {nome[::-1]}.')
    if (' ' in nome) :
        print('O seu nome contém espaços.')
    else :
        print('O seu nome não contém espaços.')
    print(f'O seu nome têm {len(nome)} caracteres.')
    print(f'A primeira letra do seu nome é {nome[0:1]}.')
    print(f'A última letra do seu nome é {nome[-1]}.')