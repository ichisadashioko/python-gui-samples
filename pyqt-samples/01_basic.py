import sys
import PyQt5
from PyQt5 import QtGui, QtWidgets

app = QtGui.QGuiApplication(sys.argv)
app.exec_()

window = QtWidgets.QWidget()
window.setGeometry(0, 0, 500, 500)
window.setWindowTitle('PyQt window')
window.show()
