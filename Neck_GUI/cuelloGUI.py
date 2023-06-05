from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget
from cuelloGUI_ui import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kargs)
        self.setupUi(self)

        self.cuello_dial.valueChanged.connect(self.actualizarLabelGiro)

    def actualizarLabelGiro(self, valor):
        self.label_giro_cuello.setText(str(valor))

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()