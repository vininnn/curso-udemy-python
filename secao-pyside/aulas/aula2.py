import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

botao = QPushButton('Botão do Eduardo')
botao.setStyleSheet('font-size: 20px;')
botao.show()

app.exec()