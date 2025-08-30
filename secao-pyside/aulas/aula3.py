import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout

app = QApplication(sys.argv)

botao = QPushButton('Botão do EduBGou')
botao.setStyleSheet('font-size: 20px;')

botao2 = QPushButton('Botão do Batata')
botao2.setStyleSheet('font-size: 20px;')

botao3 = QPushButton('Botão da Yuna')
botao3.setStyleSheet('font-size: 20px;')

central_widget = QWidget()

layout = QVBoxLayout()
central_widget.setLayout(layout)

layout.addWidget(botao)
layout.addWidget(botao2)
layout.addWidget(botao3)

central_widget.show()
app.exec()