import pyaudio,wave,time, keyboard
import speech_recognition as sr
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel
from PyQt5.QtGui import QPalette, QColor
from PyQt5 import QtCore, QtGui, QtWidgets
import threading, openai,os,sys
from gtts import gTTS
from playsound import playsound
from pygame import mixer


class MyWindow(QMainWindow):
###########################      Generar subprocesos para que no se crashe la interfaz     #################################################
    def play(self):
        self.grabacion_thread = threading.Thread(target=self.grabar_audio)
        self.grabacion_thread.start()
    def res(self):
        self.respuesta_thread = threading.Thread(target=self.generar_respuesta)
        self.respuesta_thread.start()  
#############################################   Generar Respuesta #########################################################################

    def generar_respuesta(self):
        
        openai.api_key = "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" #API Arturo 
        # Uso de ChapGPT en Python
        model_engine = "text-davinci-003"
        prompt = self.Trancripcion.text()
        
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=1,
            max_tokens=100,#tamaño de la respuesta a generar
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        print
        texto=response['choices'][0]['text']
        texto=texto.replace("\n"," ") #Remplazamos los saltos de linea por espacios en blanco para que se lea mejor el texto
        self.Respesta.setText(response['choices'][0]['text'])
        ################################################       Text to Speach           ##################################################
        NOMBRE_ARCHIVO = "sonido_generado.mp3"
        tts = gTTS(texto, lang='es-us')
        # Nota: podríamos llamar directamente a save
        tts.save(NOMBRE_ARCHIVO)
        #Reproducir audio
        #Instantiate mixer
        mixer.init()

        #Load audio file
        mixer.music.load('sonido_generado.mp3')

        #Play the music
        mixer.music.play()


        #Infinite loop
        while True:

            print("Press 'e' to exit the program")
            #take user input
            userInput = input(" ")
            if userInput == 'e':
                # Stop the music playback
                mixer.music.stop()
                print("Respuesta detenida")
                break

        mixer.quit()

    def grabar_audio(self):
        ########################################          Proceso de grabacion            ######################################
        formato = pyaudio.paInt16
        canales = 1
        tasa_muestreo = 44100
        duracion = 5  # Duración de la grabación en segundos
        nombre_archivo = "grabacion.wav"

        p = pyaudio.PyAudio()

        stream = p.open(format=formato,channels=canales,rate=tasa_muestreo,input=True,frames_per_buffer=1024)

        #print("Presiona la tecla 'G' para comenzar a grabar...")
        #keyboard.wait('g')

        print("Grabando audio...")
        frames = []

        while True:
            try:
                data = stream.read(1024)
                frames.append(data)
                if self.Parar.isDown():
                    break
            except KeyboardInterrupt:
                break

        print("Terminando la grabación...")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(nombre_archivo, 'wb')
        wf.setnchannels(canales)
        wf.setsampwidth(p.get_sample_size(formato))
        wf.setframerate(tasa_muestreo)
        wf.writeframes(b''.join(frames))
        wf.close()
        time.sleep(2)
        #####################################       Proceso de transcripcion        ############################################################

        r = sr.Recognizer()

        with sr.AudioFile("grabacion.wav") as fuente:
            audio = r.record(fuente)
        
        try:
            transcripcion = r.recognize_google(audio, language="es")
            self.Trancripcion.setText(transcripcion)
            print("Transcripción: ", transcripcion)
        except sr.UnknownValueError:
            print("No se pudo reconocer la voz.")
        except sr.RequestError as e:
            print("Error en el servicio de reconocimiento de voz: ", str(e))

    

    def _init_(self):
        super(MyWindow,self)._init_()
        self.setGeometry(200,200,800,600)

        self.setWindowTitle("Soraya")
        self.initUI()
    
    def initUI(self):     
        #Etiquetas
        self.Trancripcion = QtWidgets.QLabel(self)
        self.Trancripcion.setGeometry(QtCore.QRect(120, 30, 471, 101))
        self.Trancripcion.setText("")

        self.Respesta = QtWidgets.QLabel(self)
        self.Respesta.setGeometry(QtCore.QRect(90, 330, 581, 171))
        self.Respesta.setText("Respesta")
        
        #Botones
        self.Iniciar = QtWidgets.QPushButton(self)
        self.Iniciar.setGeometry(QtCore.QRect(280, 185, 110, 30))
        self.Iniciar.setText("Iniciar")
        self.Parar = QtWidgets.QPushButton(self)
        self.Parar.setGeometry(QtCore.QRect(410, 185, 110, 30))
        self.Parar.setText("Parar")
        self.Generar = QtWidgets.QPushButton(self)
        self.Generar.setGeometry(QtCore.QRect(335, 240, 120, 30))
        self.Generar.setText("Generar")  
         
        ############### Estilo de botones   ########################
        

        button_style = """
            QPushButton {
                border-radius: 25px;
                min-width: 50px;
                min-height: 50px;
                background-color: #5A96E7;
                color: white;
                font-family: Helvetica;
                font-size: 18px;
                font-weight: bold;
            }
            QPushButton:pressed {
                background-color: #446DA5;
            }
        """
        label_style = """
            QLabel{
                border-radius: 25px;
                min-width: 50px;
                min-height: 50px;
                background-color: white;
                color: black;
                font-family: Helvetica;
                text-align: center;
                font-size: 12px;
                  
            }
        """

        # Aplicar estilo a los botones
        self.Iniciar.setStyleSheet(button_style)
        self.Parar.setStyleSheet(button_style)
        self.Generar.setStyleSheet(button_style)
        # Aplicar estilo a las etiquetas

        self.Trancripcion.setStyleSheet(label_style)
        self.Respesta.setStyleSheet(label_style)
        #Acciones de Botones
        self.Iniciar.clicked.connect(self.play)
        self.Generar.clicked.connect(self.res)
 
#||||||||||||||||||||||||||||||||||||||||||||                Clase                    |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| 


#archivo_audio = grabar_audio()
#transcribir_audio(archivo_audio)

app = QApplication(sys.argv)
win = MyWindow()
# Establecer el color de fondo
color_fondo = QColor(210,210,210)  # Color blanco (R, G, B)
palette = QPalette()
palette.setColor(QPalette.Background, color_fondo)
win.setPalette(palette)
win.show()
sys.exit(app.exec_())
