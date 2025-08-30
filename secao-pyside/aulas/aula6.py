import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QPushButton, QWidget)

class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.central_widget = QWidget()

        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Minha janela bonita')

        self.botao = QPushButton('Botão do EduBGou')
        self.botao.setStyleSheet('font-size: 20px;')

        self.botao2 = QPushButton('Botão do Batata')
        self.botao2.setStyleSheet('font-size: 20px;')

        self.botao3 = QPushButton('Botão da Yuna')
        self.botao3.setStyleSheet('font-size: 20px;')

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.botao)
        self.grid_layout.addWidget(self.botao2)
        self.grid_layout.addWidget(self.botao3)

        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mostrar mensagem na barra')

        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu('Primeiro menu')
        self.primeira_acao = self.primeiro_menu.addAction('Primeira ação')
        self.primeira_acao.triggered.connect(self.muda_mensagem_da_status_bar)

        self.segunda_action = self.primeiro_menu.addAction('Segunda ação')
        self.segunda_action.setCheckable(True)
        self.segunda_action.toggled.connect(self.segunda_acao_marcada)
        self.segunda_action.hovered.connect(self.segunda_acao_marcada)

    @Slot()
    def muda_mensagem_da_status_bar(self):
        self.status_bar.showMessage('O meu slot foi executado')

    @Slot()
    def segunda_acao_marcada(self):
        print('Está marcado?', self.segunda_action.isChecked())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()