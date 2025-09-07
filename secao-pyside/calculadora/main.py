import sys

from display import Display
from buttons import Button
from info import Info
from window import MainWindow
from consts import WINDOW_ICON_PATH

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from style import setupTheme

if __name__ == '__main__':
    
    # Aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    # Ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    info = Info('teste')
    window.addToVLayout(info)

    # Display
    display = Display()
    window.addToVLayout(display)

    # Botões
    button = Button('Texto')
    window.addToVLayout(button)

    # Execução
    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'CompanyName.ProductName.SubProduct.VersionInformation')

    window.adjustFixedSize()
    window.show()
    app.exec()