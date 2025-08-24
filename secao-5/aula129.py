# @staticmethod
# Métodos que estão dentro da classe mas não tem acesso a self e cls

class Classe:
    @staticmethod
    def funcao_na_classe():
        print('Oi')

Classe.funcao_na_classe()