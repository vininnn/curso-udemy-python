palavra_secreta = 'pintou'

palavra_formada = '*' * len(palavra_secreta)
nova_palavra = ''
while True:
    tentativa = input('Digite uma letra: ')

    if len(tentativa) > 1:
        print('Digite apenas uma letra!')
        continue
