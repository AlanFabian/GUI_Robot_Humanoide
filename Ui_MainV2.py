# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MainV2.ui',
# licensing of 'Ui_MainV2.ui' applies.
#
# Created: Mon May 29 12:30:56 2023
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        self.dedoseleccionado=9999999
        self.distancia={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
        self.direccionseleccionada=9999999
        self.distanciaHead={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
        
        self.distancia_brazos={0:0,1:0,2:0,3:0}
        self.codoIzq=0
        self.codoDer=0        
        self.brazoselecciojnado=999999
        
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("mano_robot_imagen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setStyleSheet("background-color:rgb(45,45,45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Top_Bar.setStyleSheet("background-color:rgb(35,35,35);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toogle = QtWidgets.QFrame(self.Top_Bar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_toogle.sizePolicy().hasHeightForWidth())
        self.frame_toogle.setSizePolicy(sizePolicy)
        self.frame_toogle.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_toogle.setStyleSheet("background-color:rgb(85,170,255);")
        self.frame_toogle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toogle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toogle.setObjectName("frame_toogle")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_toogle)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Btn_Toggle = QtWidgets.QPushButton(self.frame_toogle)
        self.Btn_Toggle.setStyleSheet("color:rgb(255,255,255);\n"
"border:0xp solid;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("proximo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_Toggle.setIcon(icon)
        self.Btn_Toggle.setObjectName("Btn_Toggle")
        self.horizontalLayout_3.addWidget(self.Btn_Toggle)
        self.horizontalLayout.addWidget(self.frame_toogle)
        self.frame_Top = QtWidgets.QFrame(self.Top_Bar)
        self.frame_Top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Top.setObjectName("frame_Top")
        self.horizontalLayout.addWidget(self.frame_Top)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("background-color:rgb(35,35,35)")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Btn_Menu_3 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_Menu_3.setMinimumSize(QtCore.QSize(0, 40))
        self.Btn_Menu_3.setStyleSheet("QPushButton{\n"
"color:rgb(255,255,255);\n"
"background-color:rgb(35,35,35);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(35,170,255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"")
        
        """cambios Ricardo"""
        self.Manos = QtWidgets.QWidget(self.centralwidget)
        self.Manos.setEnabled(True)
        self.Manos.setGeometry(QtCore.QRect(100, 50, 1000, 500))
        self.Manos.setObjectName("Manos")
        self.Manos.hide()
        #Cambios propiedades del frame 
        self.Cabeza = QtWidgets.QWidget(self.centralwidget)
        self.Cabeza.setEnabled(True)
        self.Cabeza.setGeometry(QtCore.QRect(100, 50, 1200,600))
        self.Cabeza.setObjectName("Manos")
        self.Cabeza.hide()
        
        self.Inferior = QtWidgets.QWidget(self.centralwidget)
        self.Inferior.setEnabled(True)
        self.Inferior.setGeometry(QtCore.QRect(100, 50, 1000, 500))
        self.Inferior.setObjectName("Inferior")
        self.Inferior.hide()
        
        #cabeza#
        ##################################################################
        """cambios Alan"""
        self.Neck_Box = QtWidgets.QGroupBox(self.Cabeza)
        self.Neck_Box.setGeometry(QtCore.QRect(60, 40, 141, 171))
        self.Neck_Box.setFlat(False)
        self.Neck_Box.setCheckable(True)
        self.Neck_Box.setChecked(False)
        self.Neck_Box.setStyleSheet("color:rgb(255,255,255);\n"
"")
        self.Neck_Box.setObjectName("Neck_Box")
        
        self.camara = QtWidgets.QPushButton(self.Cabeza)
        self.camara.setGeometry(QtCore.QRect(200, 200, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.camara.setFont(font)
        self.camara.setObjectName("camara")
        
        self.Btn_Horizontal = QtWidgets.QPushButton(self.Neck_Box)
        self.Btn_Horizontal.setGeometry(QtCore.QRect(20, 30,110,23))
        self.Btn_Horizontal.setStyleSheet("QPushButton{color:rgb(255,255,255);\n"
"border-radius:10px ;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(35,170,255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("flecha_Horizontal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_Horizontal.setIcon(icon)
        self.Btn_Horizontal.setIconSize(QtCore.QSize(18, 18))
        self.Btn_Horizontal.setObjectName("Btn_Horizontal")
        self.Btn_Vertical = QtWidgets.QPushButton(self.Neck_Box)
        self.Btn_Vertical.setGeometry(QtCore.QRect(20,60,110,23))
        self.Btn_Vertical.setStyleSheet("QPushButton{color:rgb(255,255,255);\n"
"border-radius:10px ;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(35,170,255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("flecha_Vertical.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_Vertical.setIcon(icon1)
        self.Btn_Vertical.setIconSize(QtCore.QSize(18, 18))
        self.Btn_Vertical.setObjectName("Btn_Vertical")
        self.Btn_Horizontal_Panza_3 = QtWidgets.QPushButton(self.Neck_Box)
        self.Btn_Horizontal_Panza_3.setGeometry(QtCore.QRect(20,90,110,23))
        self.Btn_Horizontal_Panza_3.setStyleSheet("QPushButton{color:rgb(255,255,255);\n"
"border-radius:10px ;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(35,170,255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"")
        self.Btn_Horizontal_Panza_3.setIcon(icon)
        self.Btn_Horizontal_Panza_3.setIconSize(QtCore.QSize(18, 18))
        self.Btn_Horizontal_Panza_3.setObjectName("Btn_Horizontal_Panza_3")
        ###########################################################################
        self.Head = QtWidgets.QGroupBox(self.Cabeza)
        self.Head.setGeometry(QtCore.QRect(220, 40, 141, 171))
        self.Head.setFlat(False)
        self.Head.setCheckable(True)
        self.Head.setChecked(False)
        self.Head.setStyleSheet("color:rgb(255,255,255);")
        self.Head.setObjectName("Head")
        self.Btn_Horizontal_Jaw = QtWidgets.QPushButton(self.Head)
        self.Btn_Horizontal_Jaw.setGeometry(QtCore.QRect(20,30,110,23))
        self.Btn_Horizontal_Jaw.setStyleSheet("QPushButton{color:rgb(255,255,255);\n"
"border-radius:10px ;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(35,170,255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"")
        self.Btn_Horizontal_Jaw.setIcon(icon)
        self.Btn_Horizontal_Jaw.setIconSize(QtCore.QSize(18,18))
        self.Btn_Horizontal_Jaw.setObjectName("Btn_Horizontal_Jaw")
        #Groupbox Eyes 
        self.Eyes = QtWidgets.QGroupBox(self.Cabeza)
        self.Eyes.setGeometry(QtCore.QRect(385, 40, 141, 171))
        self.Eyes.setFlat(False)
        self.Eyes.setCheckable(True)
        self.Eyes.setChecked(False)
        self.Eyes.setStyleSheet("color:rgb(255,255,255);")
        self.Eyes.setObjectName("Eyes")
        
        self.Btn_Horizontal_2 = QtWidgets.QPushButton(self.Eyes)
        self.Btn_Horizontal_2.setGeometry(QtCore.QRect(20,30,110,23))
        self.Btn_Horizontal_2.setStyleSheet("QPushButton{color:rgb(255,255,255);\n"
"border-radius:10px ;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(35,170,255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"")
        self.Btn_Horizontal_2.setIcon(icon)
        self.Btn_Horizontal_2.setIconSize(QtCore.QSize(18,18))
        self.Btn_Horizontal_2.setObjectName("Btn_Horizontal_2")
        self.Btn_Vertical_2 = QtWidgets.QPushButton(self.Eyes)
        self.Btn_Vertical_2.setGeometry(QtCore.QRect(20,60,110,23))
        self.Btn_Vertical_2.setStyleSheet("QPushButton{color:rgb(255,255,255);\n"
"border-radius:10px ;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(35,170,255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"")
        self.Btn_Vertical_2.setIcon(icon1)
        self.Btn_Vertical_2.setIconSize(QtCore.QSize(18,18))
        self.Btn_Vertical_2.setObjectName("Btn_Vertical_2")
        self.horizontalSlider = QtWidgets.QSlider(self.Cabeza)
        self.horizontalSlider.setGeometry(QtCore.QRect(600,60, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.direccionhead = QtWidgets.QLabel(self.Cabeza)
        self.direccionhead.setGeometry(QtCore.QRect(650, 40, 47, 13))
        self.direccionhead.setObjectName("Direccion")
        self.direcciondistancia = QtWidgets.QLabel(self.Cabeza)
        self.direcciondistancia.setGeometry(QtCore.QRect(600, 90, 47, 13))
        self.direcciondistancia.setObjectName("direccion distancia ")
        """Aqui Termina"""
        ###############################################
        #Manos#
        self.derecha = QtWidgets.QGroupBox(self.Manos)
        self.derecha.setGeometry(QtCore.QRect(60, 40, 141, 171))
        self.derecha.setFlat(False)
        self.derecha.setCheckable(True)
        self.derecha.setChecked(False)
        self.derecha.setObjectName("derecha")
        self.pulgar2 = QtWidgets.QPushButton(self.derecha)
        self.pulgar2.setGeometry(QtCore.QRect(30, 20, 75, 23))
        self.pulgar2.setIcon(icon3)
        self.pulgar2.setIconSize(QtCore.QSize(18,18))
        self.pulgar2.setObjectName("pulgar2")
        self.pulgar2.setStyleSheet("QPushButton{color:rgb(255,255,255);\n"
"border-radius:10px ;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(35,170,255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"")
        self.indice2 = QtWidgets.QPushButton(self.derecha)
        self.indice2.setGeometry(QtCore.QRect(30, 50, 75, 23))
        self.indice2.setIcon(icon3)
        self.indice2.setIconSize(QtCore.QSize(18,18))
        self.indice2.setObjectName("indice2")
        self.indice2.setStyleSheet("QPushButton{color:rgb(255,255,255);\n"
"border-radius:10px ;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(35,170,255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"")
        self.medio2 = QtWidgets.QPushButton(self.derecha)
        self.medio2.setGeometry(QtCore.QRect(30, 80, 75, 23))
        self.medio2.setIcon(icon3)
        self.medio2.setIconSize(QtCore.QSize(18,18))
        self.medio2.setObjectName("medio2")
        self.medio2.setStyleSheet("QPushButton{color:rgb(255,255,255);\n"
"border-radius:10px ;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(35,170,255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"")
        self.anular2 = QtWidgets.QPushButton(self.derecha)
        self.anular2.setGeometry(QtCore.QRect(30, 110, 75, 23))
        self.anular2.setIcon(icon3)
        self.anular2.setIconSize(QtCore.QSize(18,18))
        self.anular2.setObjectName("anular2")
        self.anular2.setStyleSheet("QPushButton{color:rgb(255,255,255);\n"
"border-radius:10px ;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(35,170,255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"")
        self.menique2 = QtWidgets.QPushButton(self.derecha)
        self.menique2.setGeometry(QtCore.QRect(30, 140, 75, 23))
        self.menique2.setIcon(icon3)
        self.menique2.setIconSize(QtCore.QSize(18,18))
        self.menique2.setObjectName("menique2")
        self.menique2.setStyleSheet("QPushButton{color:rgb(255,255,255);\n"
"border-radius:10px ;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(35,170,255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"")
        self.izquierda = QtWidgets.QGroupBox(self.Manos)
        self.izquierda.setEnabled(True)
        self.izquierda.setGeometry(QtCore.QRect(220, 40, 141, 171))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.izquierda.setPalette(palette)
        self.izquierda.setAutoFillBackground(False)
        self.izquierda.setFlat(False)
        self.izquierda.setCheckable(True)
        self.izquierda.setChecked(False)
        self.izquierda.setObjectName("izquierda")
        self.pulgar = QtWidgets.QPushButton(self.izquierda)
        self.pulgar.setGeometry(QtCore.QRect(30, 20, 75, 23))
        self.pulgar.setIcon(icon3)
        self.pulgar.setIconSize(QtCore.QSize(18,18))
        self.pulgar.setObjectName("pulgar")
        self.pulgar.setStyleSheet("QPushButton{color:rgb(255,255,255);\n"
"border-radius:10px ;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(35,170,255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"")
        self.indice = QtWidgets.QPushButton(self.izquierda)
        self.indice.setGeometry(QtCore.QRect(30, 50, 75, 23))
        self.indice.setIcon(icon3)
        self.indice.setIconSize(QtCore.QSize(18,18))
        self.indice.setObjectName("indice")
        self.indice.setStyleSheet("QPushButton{color:rgb(255,255,255);\n"
"border-radius:10px ;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(35,170,255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"")
        self.medio = QtWidgets.QPushButton(self.izquierda)
        self.medio.setGeometry(QtCore.QRect(30, 80, 75, 23))
        self.medio.setIcon(icon3)
        self.medio.setIconSize(QtCore.QSize(18,18))
        self.medio.setObjectName("medio")
        self.medio.setStyleSheet("QPushButton{color:rgb(255,255,255);\n"
"border-radius:10px ;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(35,170,255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"")
        self.anular = QtWidgets.QPushButton(self.izquierda)
        self.anular.setGeometry(QtCore.QRect(30, 110, 75, 23))
        self.anular.setIcon(icon3)
        self.anular.setIconSize(QtCore.QSize(18,18))
        self.anular.setObjectName("anular")
        self.anular.setStyleSheet("QPushButton{color:rgb(255,255,255);\n"
"border-radius:10px ;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(35,170,255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"")
        self.menique = QtWidgets.QPushButton(self.izquierda)
        self.menique.setGeometry(QtCore.QRect(30, 140, 75, 23))
        self.menique.setIcon(icon3)
        self.menique.setIconSize(QtCore.QSize(18,18))
        self.menique.setObjectName("menique")
        self.menique.setStyleSheet("QPushButton{color:rgb(255,255,255);\n"
"border-radius:10px ;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(35,170,255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"")

        self.sliderdedo = QtWidgets.QSlider(self.Manos)
        self.sliderdedo.setGeometry(QtCore.QRect(440, 50, 160, 22))
        self.sliderdedo.setOrientation(QtCore.Qt.Horizontal)
        self.sliderdedo.setObjectName("sliderdedo")
        self.dedo = QtWidgets.QLabel(self.Manos)
        self.dedo.setGeometry(QtCore.QRect(500, 30, 47, 13))
        self.dedo.setObjectName("dedo")
        self.dedodistancia = QtWidgets.QLabel(self.Manos)
        self.dedodistancia.setGeometry(QtCore.QRect(500, 80, 47, 13))
        self.dedodistancia.setObjectName("dedodistancia")
        #Manos#
        
        #inferior#
        self.groupBoxIz = QtWidgets.QGroupBox(self.Inferior)
        self.groupBoxIz.setGeometry(QtCore.QRect(20, 20, 361, 311))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBoxIz.setFont(font)
        self.groupBoxIz.setCheckable(True)
        self.groupBoxIz.setChecked(False)
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
        self.groupBoxDer = QtWidgets.QGroupBox(self.Inferior)
        self.groupBoxDer.setGeometry(QtCore.QRect(420, 20, 361, 311))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBoxDer.setFont(font)
        self.groupBoxDer.setCheckable(True)
        self.groupBoxDer.setChecked(False)
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
        self.sliderHombroIz = QtWidgets.QSlider(self.Inferior)
        self.sliderHombroIz.setGeometry(QtCore.QRect(20, 380, 361, 22))
        self.sliderHombroIz.setMaximum(90)
        self.sliderHombroIz.setOrientation(QtCore.Qt.Horizontal)
        self.sliderHombroIz.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sliderHombroIz.setObjectName("sliderHombroIz")
        self.sliderHombroDer = QtWidgets.QSlider(self.Inferior)
        self.sliderHombroDer.setGeometry(QtCore.QRect(420, 380, 361, 22))
        self.sliderHombroDer.setMaximum(90)
        self.sliderHombroDer.setOrientation(QtCore.Qt.Horizontal)
        self.sliderHombroDer.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sliderHombroDer.setObjectName("sliderHombroDer")
        self.sliderCodoIz = QtWidgets.QSlider(self.Inferior)
        self.sliderCodoIz.setGeometry(QtCore.QRect(20, 480, 361, 22))
        self.sliderCodoIz.setMinimum(20)
        self.sliderCodoIz.setMaximum(165)
        self.sliderCodoIz.setOrientation(QtCore.Qt.Horizontal)
        self.sliderCodoIz.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sliderCodoIz.setObjectName("sliderCodoIz")
        self.sliderCodoDer = QtWidgets.QSlider(self.Inferior)
        self.sliderCodoDer.setGeometry(QtCore.QRect(420, 480, 361, 22))
        self.sliderCodoDer.setMinimum(20)
        self.sliderCodoDer.setMaximum(165)
        self.sliderCodoDer.setOrientation(QtCore.Qt.Horizontal)
        self.sliderCodoDer.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sliderCodoDer.setObjectName("sliderCodoDer")
        self.labelHombroIz = QtWidgets.QLabel(self.Inferior)
        self.labelHombroIz.setGeometry(QtCore.QRect(270, 350, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelHombroIz.setFont(font)
        self.labelHombroIz.setObjectName("labelHombroIz")
        self.labelCodoDer = QtWidgets.QLabel(self.Inferior)
        self.labelCodoDer.setGeometry(QtCore.QRect(670, 450, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCodoDer.setFont(font)
        self.labelCodoDer.setObjectName("labelCodoDer")
        self.labelHombroDer = QtWidgets.QLabel(self.Inferior)
        self.labelHombroDer.setGeometry(QtCore.QRect(670, 350, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelHombroDer.setFont(font)
        self.labelHombroDer.setObjectName("labelHombroDer")
        self.labelCodoIz = QtWidgets.QLabel(self.Inferior)
        self.labelCodoIz.setGeometry(QtCore.QRect(270, 450, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCodoIz.setFont(font)
        self.labelCodoIz.setObjectName("labelCodoIz")
        self.labelCodoMovIz = QtWidgets.QLabel(self.Inferior)
        self.labelCodoMovIz.setGeometry(QtCore.QRect(50, 450, 155, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCodoMovIz.setFont(font)
        self.labelCodoMovIz.setObjectName("labelCodoMovIz")
        self.labelCodoMovDer = QtWidgets.QLabel(self.Inferior)
        self.labelCodoMovDer.setGeometry(QtCore.QRect(450, 450, 195, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelCodoMovDer.setFont(font)
        self.labelCodoMovDer.setObjectName("labelCodoMovDer")
        self.labelHombroMovIz = QtWidgets.QLabel(self.Inferior)
        self.labelHombroMovIz.setGeometry(QtCore.QRect(50, 350, 195, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelHombroMovIz.setFont(font)
        self.labelHombroMovIz.setObjectName("labelHombroMovIz")
        self.labelHombroMovDer = QtWidgets.QLabel(self.Inferior)
        self.labelHombroMovDer.setGeometry(QtCore.QRect(450, 350, 195, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelHombroMovDer.setFont(font)
        self.labelHombroMovDer.setObjectName("labelHombroMovDer")
        #inferior#
        
        """Aqui"""
        
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Robot_Head_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_Menu_3.setIcon(icon1)
        self.Btn_Menu_3.setIconSize(QtCore.QSize(24, 24))
        self.Btn_Menu_3.setObjectName("Btn_Menu_3")
        self.verticalLayout_3.addWidget(self.Btn_Menu_3)
        self.Btn_Menu_2 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_Menu_2.setMinimumSize(QtCore.QSize(0, 40))
        self.Btn_Menu_2.setStyleSheet("QPushButton{\n"
"color:rgb(255,255,255);\n"
"background-color:rgb(35,35,35);\n"
"border-radius:10px ;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(35,170,255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("brazo-mecanico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_Menu_2.setIcon(icon2)
        self.Btn_Menu_2.setIconSize(QtCore.QSize(24, 24))
        self.Btn_Menu_2.setObjectName("Btn_Menu_2")
        self.verticalLayout_3.addWidget(self.Btn_Menu_2)
        self.Btn_Menu_1 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_Menu_1.setMinimumSize(QtCore.QSize(0, 40))
        self.Btn_Menu_1.setStyleSheet("QPushButton{\n"
"color:rgb(255,255,255);\n"
"background-color:rgb(35,35,35);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(35,170,255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(100,170,255);\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("robothand.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_Menu_1.setIcon(icon3)
        self.Btn_Menu_1.setIconSize(QtCore.QSize(24, 24))
        self.Btn_Menu_1.setObjectName("Btn_Menu_1")
        self.verticalLayout_3.addWidget(self.Btn_Menu_1)
        self.verticalLayout_2.addWidget(self.frame_top_menus)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Pages_Widget = QtWidgets.QStackedWidget(self.frame_pages)
        self.Pages_Widget.setObjectName("Pages_Widget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.Pages_Widget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.Pages_Widget.addWidget(self.page_2)
        self.verticalLayout_4.addWidget(self.Pages_Widget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
  # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.Btn_Menu_1.setText(QCoreApplication.translate("MainWindow", u"Hand", None))
        self.Btn_Menu_2.setText(QCoreApplication.translate("MainWindow", u"Arms", None))
        self.Btn_Menu_3.setText(QCoreApplication.translate("MainWindow", u"Head", None))
        
        self.derecha.setTitle(QCoreApplication.translate("MainWindow", "Mano Derecha"))
        self.pulgar2.setText(QCoreApplication.translate("MainWindow", "Pulgar"))
        self.indice2.setText(QCoreApplication.translate("MainWindow", "Indice"))
        self.medio2.setText(QCoreApplication.translate("MainWindow", "Medio"))
        self.anular2.setText(QCoreApplication.translate("MainWindow", "Anular"))
        self.menique2.setText(QCoreApplication.translate("MainWindow", "Menique"))
        self.izquierda.setTitle(QCoreApplication.translate("MainWindow", "Mano Izquierda"))
        self.pulgar.setText(QCoreApplication.translate("MainWindow", "Pulgar"))
        self.indice.setText(QCoreApplication.translate("MainWindow", "Indice"))
        self.medio.setText(QCoreApplication.translate("MainWindow", "Medio"))
        self.anular.setText(QCoreApplication.translate("MainWindow", "Anular"))
        self.menique.setText(QCoreApplication.translate("MainWindow", "Menique"))
        self.dedo.setText(QCoreApplication.translate("MainWindow", "N/A"))
        self.dedodistancia.setText(QCoreApplication.translate("MainWindow", "0"))
        
        self.Neck_Box.setTitle(QCoreApplication.translate("MainWindow","Neck"))
        self.Head.setTitle(QCoreApplication.translate("MainWindow","Jaw"))
        self.Eyes.setTitle(QCoreApplication.translate("MainWindow","Eyes"))
        
        self.direccionhead.setText(QCoreApplication.translate("MainWindow", "N/A"))
        self.direcciondistancia.setText(QCoreApplication.translate("MainWindow","0"))
        
        #Groupbox Neck
        self.Btn_Horizontal.setText(QCoreApplication.translate("MainWindow","Horizontal"))
        self.Btn_Vertical.setText(QCoreApplication.translate("MainWindow","Vertical"))
        self.Btn_Horizontal_Panza_3.setText(QCoreApplication.translate("MainWindow","Horizontal B"))
        #Group Head
        self.Btn_Horizontal_Jaw.setText(QCoreApplication.translate("MainWindow","Jaw Horizontal"))
        
        #Group Eyes
        self.camara.setText(QCoreApplication.translate("MainWindow", "camara"))
        self.Btn_Horizontal_2.setText(QCoreApplication.translate("MainWindow","Horizontal"))
        self.Btn_Vertical_2.setText(QCoreApplication.translate("MainWindow","Vertical"))
        
        
        
        self.groupBoxIz.setTitle(QCoreApplication.translate("MainWindow", "Brazo Izquierdo"))
        self.rotacionIzBoton.setText(QCoreApplication.translate("MainWindow", "Rotacion de hombro"))
        self.trasIzBoton.setText(QCoreApplication.translate("MainWindow", "Traslacion de hombro"))
        self.groupBoxDer.setTitle(QCoreApplication.translate("MainWindow", "Brazo Derecho"))
        self.rotacionDerBoton.setText(QCoreApplication.translate("MainWindow", "Rotacion de hombro"))
        self.trasDerBoton.setText(QCoreApplication.translate("MainWindow", "Traslacion de hombro"))
        
        self.labelHombroIz.setText(QCoreApplication.translate("MainWindow", "Grados"))
        self.labelCodoDer.setText(QCoreApplication.translate("MainWindow", "Grados"))
        self.labelHombroDer.setText(QCoreApplication.translate("MainWindow", "Grados"))
        self.labelCodoIz.setText(QCoreApplication.translate("MainWindow", "Grados"))
        
        self.labelCodoMovIz.setText(QCoreApplication.translate("MainWindow", "Codo Rotacion:"))
        self.labelCodoMovDer.setText(QCoreApplication.translate("MainWindow", "Codo Rotacion:"))
        self.labelHombroMovIz.setText(QCoreApplication.translate("MainWindow", "Rotacion hombro:"))
        self.labelHombroMovDer.setText(QCoreApplication.translate("MainWindow", "Rotacion hombro:"))
        
        ######################################################################################
        #self.label_1.setText(QCoreApplication.translate("MainWindow", u"PAGE 1", None))
        #self.label_2.setText(QCoreApplication.translate("MainWindow", u"PAGE 2", None))
        #self.label.setText(QCoreApplication.translate("MainWindow", u"PAGE 3", None))
    # retranslateUi