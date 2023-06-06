from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    rotHombroIz = 0
    trasHombroIz = 0
    extCodoIz = 0
    rotHombroDer = 0
    trasHombroDer = 0
    extCodoDer = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBoxIz = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxIz.setGeometry(QtCore.QRect(20, 20, 361, 311))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBoxIz.setFont(font)
        self.groupBoxIz.setCheckable(True)
        self.groupBoxIz.setObjectName("groupBoxIz")
        self.rotacionIzBoton = QtWidgets.QPushButton(self.groupBoxIz)
        self.rotacionIzBoton.setGeometry(QtCore.QRect(20, 50, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rotacionIzBoton.setFont(font)
        self.rotacionIzBoton.setObjectName("rotacionIzBoton")
        self.trasIzBoton = QtWidgets.QPushButton(self.groupBoxIz)
        self.trasIzBoton.setGeometry(QtCore.QRect(20, 140, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.trasIzBoton.setFont(font)
        self.trasIzBoton.setObjectName("TrasIzBoton")
        self.codoIzBoton = QtWidgets.QPushButton(self.groupBoxIz)
        self.codoIzBoton.setGeometry(QtCore.QRect(20, 230, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.codoIzBoton.setFont(font)
        self.codoIzBoton.setObjectName("codoIzBoton")
        self.groupBoxDer = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxDer.setGeometry(QtCore.QRect(420, 20, 361, 311))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBoxDer.setFont(font)
        self.groupBoxDer.setCheckable(True)
        self.groupBoxDer.setObjectName("groupBoxDer")
        self.rotacionDerBoton = QtWidgets.QPushButton(self.groupBoxDer)
        self.rotacionDerBoton.setGeometry(QtCore.QRect(20, 50, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rotacionDerBoton.setFont(font)
        self.rotacionDerBoton.setObjectName("rotacionDerBoton")
        self.trasDerBoton = QtWidgets.QPushButton(self.groupBoxDer)
        self.trasDerBoton.setGeometry(QtCore.QRect(20, 140, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.trasDerBoton.setFont(font)
        self.trasDerBoton.setObjectName("TrasDerBoton")
        self.codoDerBoton = QtWidgets.QPushButton(self.groupBoxDer)
        self.codoDerBoton.setGeometry(QtCore.QRect(20, 230, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.codoDerBoton.setFont(font)
        self.codoDerBoton.setObjectName("codoDerBoton")
        self.sliderHombroIz = QtWidgets.QSlider(self.centralwidget)
        self.sliderHombroIz.setGeometry(QtCore.QRect(20, 380, 361, 22))
        self.sliderHombroIz.setMaximum(90)
        self.sliderHombroIz.setOrientation(QtCore.Qt.Horizontal)
        self.sliderHombroIz.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sliderHombroIz.setObjectName("sliderHombroIz")
        self.sliderHombroDer = QtWidgets.QSlider(self.centralwidget)
        self.sliderHombroDer.setGeometry(QtCore.QRect(420, 380, 361, 22))
        self.sliderHombroDer.setMaximum(90)
        self.sliderHombroDer.setOrientation(QtCore.Qt.Horizontal)
        self.sliderHombroDer.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sliderHombroDer.setObjectName("sliderHombroDer")
        self.sliderCodoIz = QtWidgets.QSlider(self.centralwidget)
        self.sliderCodoIz.setGeometry(QtCore.QRect(20, 480, 361, 22))
        self.sliderCodoIz.setMinimum(20)
        self.sliderCodoIz.setMaximum(165)
        self.sliderCodoIz.setOrientation(QtCore.Qt.Horizontal)
        self.sliderCodoIz.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sliderCodoIz.setObjectName("sliderCodoIz")
        self.sliderCodoDer = QtWidgets.QSlider(self.centralwidget)
        self.sliderCodoDer.setGeometry(QtCore.QRect(420, 480, 361, 22))
        self.sliderCodoDer.setMinimum(20)
        self.sliderCodoDer.setMaximum(165)
        self.sliderCodoDer.setOrientation(QtCore.Qt.Horizontal)
        self.sliderCodoDer.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sliderCodoDer.setObjectName("sliderCodoDer")
        self.labelHombroIz = QtWidgets.QLabel(self.centralwidget)
        self.labelHombroIz.setGeometry(QtCore.QRect(270, 350, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelHombroIz.setFont(font)
        self.labelHombroIz.setObjectName("labelHombroIz")
        self.labelCodoDer = QtWidgets.QLabel(self.centralwidget)
        self.labelCodoDer.setGeometry(QtCore.QRect(670, 450, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCodoDer.setFont(font)
        self.labelCodoDer.setObjectName("labelCodoDer")
        self.labelHombroDer = QtWidgets.QLabel(self.centralwidget)
        self.labelHombroDer.setGeometry(QtCore.QRect(670, 350, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelHombroDer.setFont(font)
        self.labelHombroDer.setObjectName("labelHombroDer")
        self.labelCodoIz = QtWidgets.QLabel(self.centralwidget)
        self.labelCodoIz.setGeometry(QtCore.QRect(270, 450, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCodoIz.setFont(font)
        self.labelCodoIz.setObjectName("labelCodoIz")
        self.labelCodoMovIz = QtWidgets.QLabel(self.centralwidget)
        self.labelCodoMovIz.setGeometry(QtCore.QRect(50, 450, 155, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCodoMovIz.setFont(font)
        self.labelCodoMovIz.setObjectName("labelCodoMovIz")
        self.labelCodoMovDer = QtWidgets.QLabel(self.centralwidget)
        self.labelCodoMovDer.setGeometry(QtCore.QRect(450, 450, 195, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCodoMovDer.setFont(font)
        self.labelCodoMovDer.setObjectName("labelCodoMovDer")
        self.labelHombroMovIz = QtWidgets.QLabel(self.centralwidget)
        self.labelHombroMovIz.setGeometry(QtCore.QRect(50, 350, 195, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelHombroMovIz.setFont(font)
        self.labelHombroMovIz.setObjectName("labelHombroMovIz")
        self.labelHombroMovDer = QtWidgets.QLabel(self.centralwidget)
        self.labelHombroMovDer.setGeometry(QtCore.QRect(450, 350, 195, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelHombroMovDer.setFont(font)
        self.labelHombroMovDer.setObjectName("labelHombroMovDer")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.rotacionIzBoton.pressed.connect(self.cambiarRotacionIz)
        self.sliderHombroIz.valueChanged.connect(self.moverHombroIz)
        self.trasIzBoton.pressed.connect(self.cambiarTrasIz)
        self.codoIzBoton.pressed.connect(self.extenderCodoIz)
        self.sliderCodoIz.valueChanged.connect(self.moverCodoIz)

        self.rotacionDerBoton.pressed.connect(self.cambiarRotacionDer)
        self.sliderHombroDer.valueChanged.connect(self.moverHombroDer)
        self.trasDerBoton.pressed.connect(self.cambiarTrasDer)
        self.codoDerBoton.pressed.connect(self.extenderCodoDer)
        self.sliderCodoDer.valueChanged.connect(self.moverCodoDer)

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBoxIz.setTitle(_translate("MainWindow", "Brazo Izquierdo"))
        self.rotacionIzBoton.setText(_translate("MainWindow", "Rotacion de hombro"))
        self.trasIzBoton.setText(_translate("MainWindow", "Traslacion de hombro"))
        self.codoIzBoton.setText(_translate("MainWindow", "Extension de codo"))
        self.groupBoxDer.setTitle(_translate("MainWindow", "Brazo Derecho"))
        self.rotacionDerBoton.setText(_translate("MainWindow", "Rotacion de hombro"))
        self.trasDerBoton.setText(_translate("MainWindow", "Traslacion de hombro"))
        self.codoDerBoton.setText(_translate("MainWindow", "Extension de codo"))
        self.labelHombroIz.setText(_translate("MainWindow", "Grados"))
        self.labelCodoDer.setText(_translate("MainWindow", "Grados"))
        self.labelHombroDer.setText(_translate("MainWindow", "Grados"))
        self.labelCodoIz.setText(_translate("MainWindow", "Grados"))
        self.labelCodoMovIz.setText(_translate("MainWindow", "Codo:"))
        self.labelCodoMovDer.setText(_translate("MainWindow", "Codo:"))
        self.labelHombroMovIz.setText(_translate("MainWindow", "Rotacion hombro:"))
        self.labelHombroMovDer.setText(_translate("MainWindow", "Rotacion hombro:"))

    def cambiarRotacionIz(self):
        self.labelHombroMovIz.setText("Rotacion hombro:")

    def cambiarTrasIz(self):
        self.labelHombroMovIz.setText("Traslacion hombro:")
    
    def moverHombroIz(self, valor):
        self.labelHombroIz.setText(str(valor))
        if(self.rotacionIzBoton.pressed):
            self.rotHombroIz = valor
            print("Rotacion Hombro Izquierdo: " + str(self.rotHombroIz))
        else:
            if(self.trasIzBoton):
                self.trasHombroIz = valor
                print("Traslacion Hombro Izquierdo: " + str(self.trasHombroIz))
    
    def extenderCodoIz(self):
        self.labelCodoMovIz.setText("Extender Codo:")
    
    def moverCodoIz(self, valor):
        self.labelCodoIz.setText(str(valor))
        self.extCodoIz = valor
        print("Extension Codo Izquierdo: " + str(self.extCodoIz))
    
    def cambiarRotacionDer(self):
        self.labelHombroMovDer.setText("Rotacion hombro:")

    def cambiarTrasDer(self):
        self.labelHombroMovDer.setText("Traslacion hombro:")
    
    def moverHombroDer(self, valor):
        self.labelHombroDer.setText(str(valor))
        if(self.rotacionDerBoton.pressed):
            self.rotHombroDer = valor
            print("Rotacion Hombro Derecho: " + str(self.rotHombroDer))
        else:
            if(self.trasDerBoton):
                self.trasHombroDer = valor
                print("Traslacion Hombro Derecho: " + str(self.trasHombroDer))
    
    def extenderCodoDer(self):
        self.labelCodoMovDer.setText("Extender Codo:")
    
    def moverCodoDer(self, valor):
        self.labelCodoDer.setText(str(valor))
        self.extCodoDer = valor
        print("Extension Codo Derecho: " + str(self.extCodoDer))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())