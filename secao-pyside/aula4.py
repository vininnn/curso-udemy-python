import sys
from PySide6.QtWidgets import QApplication, QMainWindow ,QPushButton, QWidget, QVBoxLayout

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Janela')

botao = QPushButton('Botão do EduBGou')
botao.setStyleSheet('font-size: 20px;')

botao2 = QPushButton('Botão do Batata')
botao2.setStyleSheet('font-size: 20px;')

botao3 = QPushButton('Botão da Yuna')
botao3.setStyleSheet('font-size: 20px;')

layout = QVBoxLayout()
central_widget.setLayout(layout)

layout.addWidget(botao)
layout.addWidget(botao2)
layout.addWidget(botao3)

status_bar = window.statusBar()
status_bar.showMessage('Barra de status')

def imprimir_menu():
    print('Menu foi acionado!')

menu = window.menuBar()
primeiro_menu = menu.addMenu('Barra de menu')
acao_primeiro_menu = primeiro_menu.addAction('Primeira ação')
acao_primeiro_menu.triggered.connect(imprimir_menu)

window.show()
app.exec()