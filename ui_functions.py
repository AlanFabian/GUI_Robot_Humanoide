from main import *
class UIFunctions(MainWindow):
    def toggleMenu(self,maxWidth,enable):
        if enable:
            
            #Obtengo el ancho del frame izquierdo 
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70
            
            #definir el maximo de anchura del frame 
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard
            
            # ANIMACION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu,b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()