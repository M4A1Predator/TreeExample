from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)

w = QtGui.QWidget()
w.resize(800, 600)
w.move(300, 300)
w.setWindowTitle('Simple')
w.show()

tree = QtGui.QTreeWidget()

app.exec_()
