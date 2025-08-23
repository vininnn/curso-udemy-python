# Mantendo estados dentro de uma classe

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando!')
            return

        print(f'{self.nome} está filmando.')
        self.filmando = True
    
    def parar_de_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando!')
            return

        print(f'{self.nome} parou de filmar.')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} está filmando, ele não pode fotografar no momento!')
            return
        
        print(f'{self.nome} tirou foto.')

            
canon = Camera('Canon')
sony = Camera('Sony')
canon.filmar()
canon.filmar()
canon.fotografar()
canon.parar_de_filmar()
canon.parar_de_filmar()
sony.parar_de_filmar()
sony.fotografar()
sony.filmar()


