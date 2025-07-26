import sys

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, 
    QTextEdit, QLineEdit, QPushButton, QHBoxLayout
)

class ChatClient(QWidget):
    def __init__(self):
        # main window class
        super().__init__()
        self.setWindowTitle("PyChat - Client")
        self.setGeometry(100, 100, 400, 500)  # the first 2 is position then the next two is width and height

        # Layout and Widgets
        self.layout = QVBoxLayout()

        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)

        self.input_field = QLineEdit()
        self.input_field.setStyleSheet("font-weight: bold; font-size: 14px; color: black")
        self.input_field.setPlaceholderText("Type your message...")
        

        self.send_button = QPushButton("Send")

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_field)  # adds to the Left side
        input_layout.addWidget(self.send_button)  # adds to the Right side

        self.layout.addWidget(self.chat_display)
        self.layout.addLayout(input_layout)
        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatClient()
    window.show()
    sys.exit(app.exec_())