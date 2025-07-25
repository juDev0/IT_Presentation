"""This is the part that does the sending of signals to the slot"""
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
# from PyQt5.QtCore import QSize

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")
#         self.setFixedSize(QSize(300,300))

#         button = QPushButton("Press Me!")
#         button.setCheckable(True)  # tohhle between a checked and unchecked state when Clicked.
#         # when the button is clicked, as it is conected to the function(self.the_bu...)     
#         button.clicked.connect(self.the_button_was_clicked)  # this cliked send data, while connecting to the slot
#                                                              # that is the setCheckable(True/False)
#         self.setCentralWidget(button)


#     def the_button_was_clicked(self):
#         print("Cliked!")
    
        

# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()



"""This does the transfering of the data"""
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
# from PyQt5.QtCore import QSize
# import PyQt5.QtGui
# import sys

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
        
#         self.setWindowTitle("My App")
#         self.setFixedSize(QSize(400,400))

#         button = QPushButton("Push Me")
#         checked_ = button.setCheckable(True)
#         button.clicked.connect(self.the_button_was_clicked)
#         button.clicked.connect(self.the_button_was_toggled)
#         self.setCentralWidget(button)


#     def the_button_was_clicked(self):
#         print("Clicked!")

#     def the_button_was_toggled(self,checked):
#         # checked is a toggle that returnes a ture/false state
#         print("Checked?",checked)

#             OR             
    # def the_button_was_clicked(self,checked_):
    #     print("Clicked!")
    #     print(f"Clicked? {checked_}")  
        

# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()


"""Using the 'clicked' signal"""

# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
# from PyQt5.QtCore import QSize
# import PyQt5.QtGui
# import sys
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.button_is_checked = True  # this button will return 
#         # the value of the checked parameter in which, will change in respect to that parameter.

#         self.setWindowTitle("My App")

#         button = QPushButton("Press Me!")
#         button.setCheckable(True)  # this one like makes the clicked signal 
#         # return a data in a True state because by default, it returns a False state.
#         button.clicked.connect(self.the_button_was_toggled)
#         button.setChecked(self.button_is_checked)

#         self.setCentralWidget(button)

#     def the_button_was_toggled(self, checked):
#         self.button_is_checked = checked

#         print(self.button_is_checked)


# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()


"""Using the 'released' signal we customize"""
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
# from PyQt5.QtCore import QSize
# import PyQt5.QtGui
# import sys

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
        
#         self.button_is_checked = True

#         self.setWindowTitle("My App")

#         self.button = QPushButton("Press Me!")
#         self.button.setCheckable(True)
#         self.button.released.connect(self.the_button_was_realeased)
#         self.button.setChecked(self.button_is_checked)

#         self.setCentralWidget(self.button)

#     def the_button_was_realeased(self):
#         self.button_is_checked = self.button.isChecked()
#         print(self.button_is_checked)

# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()



"""Changing the interface"""
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
# from PyQt5.QtCore import QSize
# from PyQt5.QtGui import QFont
# import sys

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My App")
#         self.setFixedSize(QSize(300,300))

#         self.button = QPushButton("Press Me!")
#         self.button.clicked.connect(self.the_button_was_clicked)
#         self.setCentralWidget(self.button)

#     def the_button_was_clicked(self):
#         self.button.setText("You already ckicked me. ")
#         self.button.setEnabled(False)

#         self.setWindowTitle("My Oneshot App! ")
#         self.setWindowTitle("A new window Title")
        

# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()



from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont

from random import choice

import sys

window_titles = [
    "My App",
    "My App",
    "Still My App",
    "Still My App",
    "What on earth",
    "What on earth",
    "This is supuising",
    "This is suprising",
    "Something Went wrong"
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.n_times_clicked = 0

        self.setWindowTitle("My App") 
        self.setFixedSize(QSize(300,300))

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)
        self.setCentralWidget(self.button)

        self.windowTitleChanged.connect(self.the_window_title_changed)

    def the_button_was_clicked(self):
        print("Clicked!")
        new_window_title = choice(window_titles)
        self.button.setText("You already ckicked me. ")
        
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self,window_title):
        print(f"Window title changed: {window_title}")

        if window_title ==  "Something Went wrong":
            self.button.setDisabled(True)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()