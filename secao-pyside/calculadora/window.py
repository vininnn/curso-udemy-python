from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__ (self, parents: QWidget | None = None, *args, **kwargs):
        super().__init__(parents, *args, **kwargs)

        self.central_widget = QWidget()
        self.verticalLayout = QVBoxLayout()
        self.central_widget.setLayout(self.verticalLayout)
        self.setCentralWidget(self.central_widget)

        self.setWindowTitle('Calculadora')
        #self.setWindowIcon(./files/calculadora_icon.png)

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.verticalLayout.addWidget(widget)