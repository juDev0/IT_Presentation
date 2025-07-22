from PyQt5.QtWidgets import QApplication, QWidget

# Only needed for access to command line arguments
import sys

# receive command-line args form terminal
# and pass them into the application
app = QApplication(sys.argv)

# this will create the window of the QApplication
window = QWidget() 

# default, the window is always hidden so, you show
window.show()

# start the event loop
app.exec()