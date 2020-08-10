"""
Entry point for GUI main window
"""

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

class SliceNDiceMainWindow(QMainWindow):
    """
    Main window class for slice n' dice
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Slice n\' Dice')
        screen = QApplication.primaryScreen().availableGeometry()

        (height, width) = (screen.height(), screen.width())

        self.setFixedHeight(height - 50)
        self.setFixedWidth(width * 0.75)
        self.move((width - width * 0.75) / 2.0, 0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SliceNDiceMainWindow()
    window.show()
    app.exec_()
