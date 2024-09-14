#aqui hacemos la importacion de todo lo que vamos a utilizar 
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QMessageBox

class VentanaDatosPersona(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Datos de la Persona")  #  aqui va el título de la ventana
        self.setGeometry(100, 100, 400, 500)  # aqui es para colocar el tamaño de la ventana

        layout = QVBoxLayout()  # este es para que el layout sea vertical

        # aqui pusimos una lista de datos a solicitar
        self.datos = ["Nombre", "Edad", "Género", "Nacionalidad", "Profesión", "Dirección", "Teléfono", "Correo Electrónico", "Estado Civil", "Ocupación"]
        
        # este es  un diccionario para guardar las entradas de los QLineEdit
        self.entradas = {}

        # aqui creamos una entrada para cada dato
        for dato in self.datos:
            layout.addWidget(QLabel(dato + ":", self))  # esta es la etiqueta del dato
            entrada = QLineEdit(self)  # esta es la entrada de texto
            layout.addWidget(entrada)
            self.entradas[dato] = entrada  # y aqui es donde se guarda la entrada en el diccionario

        # este es el boton para enviar y mostrar los datos
        boton_enviar = QPushButton("Ver Datos", self)
        boton_enviar.clicked.connect(self.mostrar_datos)
        layout.addWidget(boton_enviar)

        self.setLayout(layout)

    def mostrar_datos(self):
        # aqui lo hicimos para crear un mensaje con los datos que se han ingresados ingresados
        mensaje = ""
        for dato, entrada in self.entradas.items():
            valor = entrada.text()  # aqui se obtener el texto ingresado
            mensaje += f"{dato}: {valor}\n"

        # con este nosotros mostramos los datos ingresados en un mensaje emergente
        QMessageBox.information(self, "Datos Ingresados", mensaje)

app = QApplication(sys.argv)
ventana = VentanaDatosPersona()
ventana.show()  # mostramos la ventana
sys.exit(app.exec_())  # iniciamos el ciclo de eventos