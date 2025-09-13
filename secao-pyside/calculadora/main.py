import sys

from display import Display
from buttons import ButtonsGrid
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

    # Info
    info = Info('teste')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttons_grid = ButtonsGrid()
    window.verticalLayout.addLayout(buttons_grid)

    # Execução
    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'CompanyName.ProductName.SubProduct.VersionInformation')

    window.adjustFixedSize()
    window.show()
    app.exec()