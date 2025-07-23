import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(QSize(300,300))

        button = QPushButton("Press Me!")
        button.setCheckable(True)  # tohhle between a checked and unchecked state when Clicked.
        # when the button is clicked, as it is conected to the function(self.the_bu...)     
        button.clicked.connect(self.the_button_was_clicked)  # this cliked send data, while connecting to the slot
                                                             # that is the setCheckable(True/False)
        self.setCentralWidget(button)


    def the_button_was_clicked(self, cliked_):
        print("Cliked!")
        
        # if cliked_ == True:
        #     print("Power on")
        #     cliked_
          
        # else:
        #     print("Power off") 
        #     cliked_   


        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()