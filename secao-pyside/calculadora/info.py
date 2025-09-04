from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt

from consts import SMALL_FONT_SIZE

class Info(QLabel):
    def __init__ (self, text:str, parents: QWidget | None = None, *args, **kwargs):
        super().__init__(text, parents, *args, **kwargs)
        self.defineStyle()

    def defineStyle(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)