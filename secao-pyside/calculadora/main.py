import sys

from window import MainWindow
from consts import WINDOW_ICON_PATH

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'CompanyName.ProductName.SubProduct.VersionInformation')

    window.adjustFixedSize()
    window.show()
    app.exec()