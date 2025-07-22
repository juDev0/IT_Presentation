"""A normal application interface"""
# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *

# # Only needed for access to command line arguments
# import sys

# # receive command-line args form terminal
# # and pass them into the application
# app = QApplication(sys.argv)

# # this will create the window of the QApplication
# window = QWidget() 

# # default, the window is always hidden so, you show
# window.show()

# # start the event loop
# app.exec()



"""This proves that you still will have a window without QWidget"""
import sys 
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import *
from PyQt5.QtGui import *

app = QApplication(sys.argv)
window = QPushButton("Push Me")
window.show()
app.exec()
