from main import *
from gui_camara_2 import App


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
            
    def show_manos(self):
        self.ui.Manos.show()
        self.ui.Inferior.hide()
        self.ui.Cabeza.hide()
        
    def show_inferior(self):
        self.ui.Inferior.show()
        self.ui.Manos.hide()
        self.ui.Cabeza.hide()
            
    def show_cabeza(self):
        self.ui.Cabeza.show()
        self.ui.Manos.hide()
        self.ui.Inferior.hide()
            
        
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
        
    def cambiarDedo0(self):
        self.ui.dedo.setText("Pulgar Izquierdo")
        self.ui.dedo.adjustSize()
        self.ui.dedoseleccionado=0
        self.ui.dedodistancia.setText(str(self.ui.distancia[0]))
        self.ui.sliderdedo.setSliderPosition(self.ui.distancia[0])
    
    def cambiarDedo1(self):
        self.ui.dedo.setText("Indice Izquierdo")
        self.ui.dedo.adjustSize()
        self.ui.dedoseleccionado=1
        self.ui.dedodistancia.setText(str(self.ui.distancia[1]))
        self.ui.sliderdedo.setSliderPosition(self.ui.distancia[1])
        
    def cambiarDedo2(self):
        self.ui.dedo.setText("Medio Izquierdo")
        self.ui.dedo.adjustSize()
        self.ui.dedoseleccionado=2
        self.ui.dedodistancia.setText(str(self.ui.distancia[2]))
        self.ui.sliderdedo.setSliderPosition(self.ui.distancia[2])
        
    def cambiarDedo3(self):
        self.ui.dedo.setText("Anular Izquierdo")
        self.ui.dedo.adjustSize()
        self.ui.dedoseleccionado=3
        self.ui.dedodistancia.setText(str(self.ui.distancia[3]))
        self.ui.sliderdedo.setSliderPosition(self.ui.distancia[3])
        
    def cambiarDedo4(self):
        self.ui.dedo.setText("Menique Izquierdo")
        self.ui.dedo.adjustSize()
        self.ui.dedoseleccionado=4
        self.ui.dedodistancia.setText(str(self.ui.distancia[4]))
        self.ui.sliderdedo.setSliderPosition(self.ui.distancia[4])
        
        
        
    def cambiarDedo0_2(self):
        self.ui.dedo.setText("Pulgar Derecho")
        self.ui.dedo.adjustSize()
        self.ui.dedoseleccionado=5
        self.ui.dedodistancia.setText(str(self.ui.distancia[5]))
        self.ui.sliderdedo.setSliderPosition(self.ui.distancia[5])
    
    def cambiarDedo1_2(self):
        self.ui.dedo.setText("Indice Derecho")
        self.ui.dedo.adjustSize()
        self.ui.dedoseleccionado=6
        self.ui.dedodistancia.setText(str(self.ui.distancia[6]))
        self.ui.sliderdedo.setSliderPosition(self.ui.distancia[6])
        
    def cambiarDedo2_2(self):
        self.ui.dedo.setText("Medio Derecho")
        self.ui.dedo.adjustSize()
        self.ui.dedoseleccionado=7
        self.ui.dedodistancia.setText(str(self.ui.distancia[7]))
        self.ui.sliderdedo.setSliderPosition(self.ui.distancia[7])
        
    def cambiarDedo3_2(self):
        self.ui.dedo.setText("Anular Derecho")
        self.ui.dedo.adjustSize()
        self.ui.dedoseleccionado=8
        self.ui.dedodistancia.setText(str(self.ui.distancia[8]))
        self.ui.sliderdedo.setSliderPosition(self.ui.distancia[8])
        
    def cambiarDedo4_2(self):
        self.ui.dedo.setText("Menique Derecho")
        self.ui.dedo.adjustSize()
        self.ui.dedoseleccionado=9
        self.ui.dedodistancia.setText(str(self.ui.distancia[9]))
        self.ui.sliderdedo.setSliderPosition(self.ui.distancia[9])
    #Funciones Neck
    def change_Horizontal_direction(self):
        self.ui.direccionhead.setText("Horizontal en el eje de la cabeza")
        self.ui.direccionhead.adjustSize()
        self.ui.direccionseleccionada=0
        self.ui.direcciondistancia.setText(str(self.ui.distanciaHead[0]))
        self.ui.horizontalSlider.setSliderPosition(self.ui.distanciaHead[0])
        
    def change_Vertical_direction(self):
        self.ui.direccionhead.setText("Vertical en el eje de la cabeza")
        self.ui.direccionhead.adjustSize()
        self.ui.direccionseleccionada=1
        self.ui.direcciondistancia.setText(str(self.ui.distanciaHead[1]))
        self.ui.horizontalSlider.setSliderPosition(self.ui.distanciaHead[1])
        
    def change_Horizontal_directionBelly(self):
        self.ui.direccionhead.setText("Horizontal desde el eje del pecho")
        self.ui.direccionhead.adjustSize()
        self.ui.direccionseleccionada=2
        self.ui.direcciondistancia.setText(str(self.ui.distanciaHead[2]))
        self.ui.horizontalSlider.setSliderPosition(self.ui.distanciaHead[2])
    
    #Funciones Head
    def change_HorizontalJaw(self):
        self.ui.direccionhead.setText("Horizontal Mandibula")
        self.ui.direccionhead.adjustSize()
        self.ui.direccionseleccionada=3
        self.ui.direcciondistancia.setText(str(self.ui.distanciaHead[3]))
        self.ui.horizontalSlider.setSliderPosition(self.ui.distanciaHead[3])
    #Funciones Eyes
    
    def change_Horizontal_direction_Eyes(self):
        self.ui.direccionhead.setText("Horizontal Ojos")
        self.ui.direccionhead.adjustSize()
        self.ui.direccionseleccionada=4
        self.ui.direcciondistancia.setText(str(self.ui.distanciaHead[4]))
        self.ui.horizontalSlider.setSliderPosition(self.ui.distanciaHead[4])
    
    def change_Vertical_direction_Eyes(self):
        self.ui.direccionhead.setText("Vertical Ojos")
        self.ui.direccionhead.adjustSize()
        self.ui.direccionseleccionada=5
        self.ui.direcciondistancia.setText(str(self.ui.distanciaHead[5]))
        self.ui.horizontalSlider.setSliderPosition(self.ui.distanciaHead[5])

    def mover_dedos(self,value):
        print(self.ui.distancia)
        if self.ui.dedoseleccionado==0:
            self.ui.dedodistancia.setText(str(value))
            self.ui.distancia[0]=value
        if self.ui.dedoseleccionado==1:
            self.ui.dedodistancia.setText(str(value))
            self.ui.distancia[1]=value
        if self.ui.dedoseleccionado==2:
            self.ui.dedodistancia.setText(str(value))
            self.ui.distancia[2]=value
        if self.ui.dedoseleccionado==3:
            self.ui.dedodistancia.setText(str(value))
            self.ui.distancia[3]=value
        if self.ui.dedoseleccionado==4:
            self.ui.dedodistancia.setText(str(value))
            self.ui.distancia[4]=value
            
        if self.ui.dedoseleccionado==5:
            self.ui.dedodistancia.setText(str(value))
            self.ui.distancia[5]=value
        if self.ui.dedoseleccionado==6:
            self.ui.dedodistancia.setText(str(value))
            self.ui.distancia[6]=value
        if self.ui.dedoseleccionado==7:
            self.ui.dedodistancia.setText(str(value))
            self.ui.distancia[7]=value
        if self.ui.dedoseleccionado==8:
            self.ui.dedodistancia.setText(str(value))
            self.ui.distancia[8]=value
        if self.ui.dedoseleccionado==9:
            self.ui.dedodistancia.setText(str(value))
            self.ui.distancia[9]=value
    #Cambios Alan 
    ######################################################
    def change_directions(self,value):
        if self.ui.direccionseleccionada==0:
            self.ui.direcciondistancia.setText(str(value))
            self.ui.distanciaHead[0]=value
        if self.ui.direccionseleccionada==1:
            self.ui.direcciondistancia.setText(str(value))
            self.ui.distanciaHead[1]=value
        if self.ui.direccionseleccionada==2:
            self.ui.direcciondistancia.setText(str(value))
            self.ui.distanciaHead[2]=value
        if self.ui.direccionseleccionada==3:
            self.ui.direcciondistancia.setText(str(value))
            self.ui.distanciaHead[3]=value
        if self.ui.direccionseleccionada==4:
            self.ui.direcciondistancia.setText(str(value))
            self.ui.distanciaHead[4]=value
            
        if self.ui.direccionseleccionada==5:
            self.ui.direcciondistancia.setText(str(value))
            self.ui.distanciaHead[5]=value
        if self.ui.direccionseleccionada==6:
            self.ui.direcciondistancia.setText(str(value))
            self.ui.distanciaHead[6]=value
            
    #Brazos
    
    def cambiarRotacion0(self):
        self.ui.labelHombroMovDer.setText("Rotacion hombro:")
        self.ui.labelHombroMovDer.adjustSize()
        self.ui.brazoseleccionado=0
        self.ui.labelHombroDer.setText(str(self.ui.distancia_brazos[0]))
        self.ui.sliderHombroDer.setSliderPosition(self.ui.distancia_brazos[0])
    
    def cambiarTraslacion1(self):
        self.ui.labelHombroMovDer.setText("Traslacion hombro:")
        self.ui.labelHombroMovDer.adjustSize()
        self.ui.brazoseleccionado=1
        self.ui.labelHombroDer.setText(str(self.ui.distancia_brazos[1]))
        self.ui.sliderHombroDer.setSliderPosition(self.ui.distancia_brazos[1])
        
    def cambiarRotacion2(self):
        self.ui.labelHombroMovIz.setText("Rotacion hombro:")
        self.ui.labelHombroMovIz.adjustSize()
        self.ui.brazoseleccionado=2
        self.ui.labelHombroIz.setText(str(self.ui.distancia_brazos[2]))
        self.ui.sliderHombroIz.setSliderPosition(self.ui.distancia_brazos[2])
    
    def cambiarTraslacion3(self):
        self.ui.labelHombroMovIz.setText("Traslacion hombro:")
        self.ui.labelHombroMovIz.adjustSize()
        self.ui.brazoseleccionado=3
        self.ui.labelHombroIz.setText(str(self.ui.distancia_brazos[3]))
        self.ui.sliderHombroIz.setSliderPosition(self.ui.distancia_brazos[3])

    def mover_hombro(self,value):
        if self.ui.brazoseleccionado==0:
            self.ui.labelHombroDer.setText(str(value))
            self.ui.distancia_brazos[0]=value
        if self.ui.brazoseleccionado==1:
            self.ui.labelHombroDer.setText(str(value))
            self.ui.distancia_brazos[1]=value
        if self.ui.brazoseleccionado==2:
            self.ui.labelHombroIz.setText(str(value))
            self.ui.distancia_brazos[2]=value
        if self.ui.brazoseleccionado==3:
            self.ui.labelHombroIz.setText(str(value))
            self.ui.distancia_brazos[3]=value
            
    def moverCodoIz(self,value):
        self.ui.labelCodoIz.setText(str(value))
        self.ui.codoIzq=value  
        
        
    def moverCodoDer(self,value):
        self.ui.labelCodoDer.setText(str(value))
        self.ui.codoDer=value
        
    def window2(self):
        self.w = App()
        self.w.show()