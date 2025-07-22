"""A normal application interface 1"""
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



"""This proves that you still will have a window without QWidget 2"""
# import sys 
# from PyQt5.QtWidgets import QApplication, QPushButton
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *

# app = QApplication(sys.argv)
# window = QPushButton("Push Me")
# window.show()
# app.exec()


"""Doing the same thing but with a class 3"""
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *

# import sys  


# class MainWindow(QMainWindow):

#     # def __init__(self, *args, **Kwargs):
#        # super(MainWindow, self).__init__(*args, **Kwargs)

#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("my Awsone App")


# app = QApplication(sys.argv)
# MainWindow = MainWindow()
# MainWindow.show()
# app.exec()



"""This futher explains the 4"""
# import sys 
# from PyQt5.QtCore import QSize, Qt
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

# # Subclass QMainWindow to customize your application's moin window
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
        
#         self.setWindowTitle("My App")

#         button = QPushButton("Press Me!")
#         # Set the central widget of the window.
#         self.setCentralWidget(button)
        


# app= QApplication(sys.argv)  # This enables us to Event Loop
# window= MainWindow()  # THis, will take the Moin Object of the sub class of the MainWindow
# window.show()
# app.exec()



"""This shows us 5"""
import sys 
from PyQt5.QtCore import QSize, Qt  # this is on the configuration a bit...
import PyQt5.QtGui  # this is on the Graphics
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        # it sets the size of the window
        self.setFixedSize(QSize(500,200))
        # self.setMinimumSize(QSize(565,565))
        # self.setMaximumSize(QSize(565,565))

        button = QPushButton("Press Me!")
        self.setCentralWidget(button)
        
        
app = QApplication(sys.argv)
window= MainWindow()
window.show()
app.exec()