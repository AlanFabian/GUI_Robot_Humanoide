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
            
    def show_superior(self):
        self.ui.Superior.show()
        self.ui.Inferior.hide()
        self.ui.Cabeza.hide()
        
    def show_inferior(self):
        self.ui.Inferior.show()
        self.ui.Superior.hide()
        self.ui.Cabeza.hide()
            
    def show_cabeza(self):
        self.ui.Cabeza.show()
        self.ui.Superior.hide()
        self.ui.Inferior.hide()
            
    def mover_dedo1(self,value):
        dedo1_movimiento=value
        self.ui.dedo1_desplazamiento.setText(str(dedo1_movimiento))
        
    def mover_dedo2(self,value):
        dedo2_movimiento=value
        self.ui.dedo2_desplazamiento.setText(str(dedo2_movimiento))
        
    def mover_hombro(self,value):
        hombro_movimiento=value
        self.ui.hombro_desplazamiento.setText(str(hombro_movimiento))
        
    def mover_codo(self,value):
        codo_movimiento=value
        self.ui.codo_desplazamiento.setText(str(codo_movimiento))
    
    def mover_cuello(self,value):
        cuello_movimiento=value
        self.ui.cuello_desplazamiento.setText(str(cuello_movimiento))
        
    def mover_ojos(self,value):
        ojos_movimiento=value
        self.ui.ojos_desplazamiento.setText(str(ojos_movimiento))
