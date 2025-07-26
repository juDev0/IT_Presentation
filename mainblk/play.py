import sys
from PyQt5.QtCore import QSize
import PyQt5
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton,
    QTextEdit, QLineEdit, QVBoxLayout,
    QHBoxLayout
)

class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_pushed = True

        self.setFixedSize(QSize(200,200))
        self.setWindowTitle("My App!")

        self.button = QPushButton("Push Me!")
        self.button.setCheckable(True)  # this activates the Checkable state
        self.button.released.connect(self.button_Toggled)
        self.button.setChecked(self.button_pushed)  # this just passes a signal that seems as though its been flipped
        self.button.setStyleSheet("font-weight: bold; font-size: 14px; color: black")

        self.setCentralWidget(self.button)    

    def button_Toggled(self):
        self.button_pushed = self.button.isChecked()  # it returns the data in respect to setChecked()
        print(self.button_pushed)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindows()
    window.show()
    app.exec()