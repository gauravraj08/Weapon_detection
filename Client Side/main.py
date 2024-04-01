from PyQt5.QtWidgets import QApplication
import sys
from login_window import LogInWindow

app = QApplication(sys.argv)
mainwindow = LogInWindow()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")