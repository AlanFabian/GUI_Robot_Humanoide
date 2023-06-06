from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget
from bicepsGUI_ui import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kargs)
        self.setupUi(self)

        self.bicepIzquierdoSlider.valueChanged.connect(self.actualizarLabelIzquierdo)
        self.bicepDerechoSlider.valueChanged.connect(self.actualizarLabelDerecho)
        self.bicepIzquierdoRadio.toggled.connect(self.habilitarBicep)
        self.bicepDerechoRadio.toggled.connect(self.habilitarBicep)

    def actualizarLabelIzquierdo(self, valor):
        self.bicepIzquierdoLabel.setText(str(valor))
    
    def actualizarLabelDerecho(self, valor):
        self.bicepDerechoLabel.setText(str(valor))

    def habilitarBicep(self):
        if self.bicepIzquierdoRadio.isChecked():
            self.bicepIzquierdoLabel.setEnabled(True)
            self.bicepIzquierdoSlider.setEnabled(True)
            self.bicepDerechoLabel.setEnabled(False)
            self.bicepDerechoSlider.setEnabled(False)
        else: 
            if self.bicepDerechoRadio.isChecked():
                self.bicepIzquierdoLabel.setEnabled(False)
                self.bicepIzquierdoSlider.setEnabled(False)
                self.bicepDerechoLabel.setEnabled(True)
                self.bicepDerechoSlider.setEnabled(True)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()