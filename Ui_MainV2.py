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
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
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
"border:0xp solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(35,170,255);\n"
"}")
        
        """cambios"""
        self.Superior = QtWidgets.QWidget(self.centralwidget)
        self.Superior.setEnabled(True)
        self.Superior.setGeometry(QtCore.QRect(100, 50, 271, 321))
        self.Superior.setObjectName("Superior")
        self.Superior.hide()
        
        self.Cabeza = QtWidgets.QWidget(self.centralwidget)
        self.Cabeza.setEnabled(True)
        self.Cabeza.setGeometry(QtCore.QRect(100, 50, 271, 321))
        self.Cabeza.setObjectName("Superior")
        self.Cabeza.hide()
        
        self.Inferior = QtWidgets.QWidget(self.centralwidget)
        self.Inferior.setEnabled(True)
        self.Inferior.setGeometry(QtCore.QRect(100, 50, 271, 321))
        self.Inferior.setObjectName("Inferior")
        self.Inferior.hide()
        
        #cabeza#
        self.ojos = QtWidgets.QSlider(self.Cabeza)
        self.ojos.setGeometry(QtCore.QRect(50, 90, 160, 22))
        self.ojos.setOrientation(QtCore.Qt.Horizontal)
        self.ojos.setObjectName("ojos")
        
        self.cuello = QtWidgets.QSlider(self.Cabeza)
        self.cuello.setGeometry(QtCore.QRect(30, 190, 160, 22))
        self.cuello.setOrientation(QtCore.Qt.Horizontal)
        self.cuello.setObjectName("cuello")
        
        self.cuello_desplazamiento = QtWidgets.QLabel(self.Cabeza)
        self.cuello_desplazamiento.setGeometry(QtCore.QRect(50, 290, 47, 13))
        self.cuello_desplazamiento.setObjectName("cabeza_desplazamiento")
        self.cuello_desplazamiento.setStyleSheet("color: white;")
        
        self.cuello_label = QtWidgets.QLabel(self.Cabeza)
        self.cuello_label.setGeometry(QtCore.QRect(50, 180, 47, 13))
        self.cuello_label.setObjectName("cabeza_label")
        self.cuello_label.setStyleSheet("color: white;")
        
        self.ojos_label = QtWidgets.QLabel(self.Cabeza)
        self.ojos_label.setGeometry(QtCore.QRect(110, 70, 47, 13))
        self.ojos_label.setObjectName("ojos_label")
        self.ojos_label.setStyleSheet("color: white;")
        
        self.ojos_desplazamiento = QtWidgets.QLabel(self.Cabeza)
        self.ojos_desplazamiento.setGeometry(QtCore.QRect(110, 120, 47, 13))
        self.ojos_desplazamiento.setObjectName("ojos_desplazamiento")
        self.ojos_desplazamiento.setStyleSheet("color: white;")
        #cabeza#
        
        #superior#
        self.dedo1 = QtWidgets.QSlider(self.Superior)
        self.dedo1.setGeometry(QtCore.QRect(50, 90, 160, 22))
        self.dedo1.setOrientation(QtCore.Qt.Horizontal)
        self.dedo1.setObjectName("dedo1")
        
        self.dedo2 = QtWidgets.QSlider(self.Superior)
        self.dedo2.setGeometry(QtCore.QRect(30, 190, 160, 22))
        self.dedo2.setOrientation(QtCore.Qt.Horizontal)
        self.dedo2.setObjectName("dedo2")
        
        self.dedo2_desplazamiento = QtWidgets.QLabel(self.Superior)
        self.dedo2_desplazamiento.setGeometry(QtCore.QRect(50, 290, 47, 13))
        self.dedo2_desplazamiento.setObjectName("dedo2_desplazamiento")
        self.dedo2_desplazamiento.setStyleSheet("color: white;")
        
        self.dedo2_label = QtWidgets.QLabel(self.Superior)
        self.dedo2_label.setGeometry(QtCore.QRect(50, 180, 47, 13))
        self.dedo2_label.setObjectName("dedo2_label")
        self.dedo2_label.setStyleSheet("color: white;")
        
        self.dedo1_label = QtWidgets.QLabel(self.Superior)
        self.dedo1_label.setGeometry(QtCore.QRect(110, 70, 47, 13))
        self.dedo1_label.setObjectName("dedo1_label")
        self.dedo1_label.setStyleSheet("color: white;")
        
        self.dedo1_desplazamiento = QtWidgets.QLabel(self.Superior)
        self.dedo1_desplazamiento.setGeometry(QtCore.QRect(110, 120, 47, 13))
        self.dedo1_desplazamiento.setObjectName("dedo1_desplazamiento")
        self.dedo1_desplazamiento.setStyleSheet("color: white;")
        #superior#
        
        #inferior#
        self.hombro = QtWidgets.QSlider(self.Inferior)
        self.hombro.setGeometry(QtCore.QRect(30, 190, 160, 22))
        self.hombro.setOrientation(QtCore.Qt.Horizontal)
        self.hombro.setObjectName("hombro")
        
        self.hombro_desplazamiento = QtWidgets.QLabel(self.Inferior)
        self.hombro_desplazamiento.setGeometry(QtCore.QRect(50, 290, 47, 13))
        self.hombro_desplazamiento.setObjectName("hombro_desplazamiento")
        self.hombro_desplazamiento.setStyleSheet("color: white;")
        
        self.hombro_label = QtWidgets.QLabel(self.Inferior)
        self.hombro_label.setGeometry(QtCore.QRect(50, 180, 47, 13))
        self.hombro_label.setObjectName("hombro_label")
        self.hombro_label.setStyleSheet("color: white;")
        
        self.codo = QtWidgets.QSlider(self.Inferior)
        self.codo.setGeometry(QtCore.QRect(50, 90, 160, 22))
        self.codo.setOrientation(QtCore.Qt.Horizontal)
        self.codo.setObjectName("codo")
        
        self.codo_label = QtWidgets.QLabel(self.Inferior)
        self.codo_label.setGeometry(QtCore.QRect(110, 70, 47, 13))
        self.codo_label.setObjectName("codo_label")
        self.codo_label.setStyleSheet("color: white;")
        
        self.codo_desplazamiento = QtWidgets.QLabel(self.Inferior)
        self.codo_desplazamiento.setGeometry(QtCore.QRect(110, 120, 47, 13))
        self.codo_desplazamiento.setObjectName("codo_desplazamiento")
        self.codo_desplazamiento.setStyleSheet("color: white;")
        #inferior#
        
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
"border:0xp solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(35,170,255);\n"
"}")
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
"border:0xp solid;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(35,170,255);\n"
"}")
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
        
        self.dedo2_desplazamiento.setText(QCoreApplication.translate("MainWindow", "0"))
        self.dedo2_label.setText(QCoreApplication.translate("MainWindow", "dedo2"))
        self.dedo1_label.setText(QCoreApplication.translate("MainWindow", "dedo1"))
        self.dedo1_desplazamiento.setText(QCoreApplication.translate("MainWindow", "0"))
        
        self.hombro_desplazamiento.setText(QCoreApplication.translate("MainWindow", "0"))
        self.hombro_label.setText(QCoreApplication.translate("MainWindow", "Hombro"))
        self.codo_label.setText(QCoreApplication.translate("MainWindow", "Codo"))
        self.codo_desplazamiento.setText(QCoreApplication.translate("MainWindow", "0"))
        
        self.cuello_desplazamiento.setText(QCoreApplication.translate("MainWindow", "0"))
        self.cuello_label.setText(QCoreApplication.translate("MainWindow", "cuello"))
        self.ojos_label.setText(QCoreApplication.translate("MainWindow", "Ojos"))
        self.ojos_desplazamiento.setText(QCoreApplication.translate("MainWindow", "0"))
        ######################################################################################
        #self.label_1.setText(QCoreApplication.translate("MainWindow", u"PAGE 1", None))
        #self.label_2.setText(QCoreApplication.translate("MainWindow", u"PAGE 2", None))
        #self.label.setText(QCoreApplication.translate("MainWindow", u"PAGE 3", None))
    # retranslateUi
