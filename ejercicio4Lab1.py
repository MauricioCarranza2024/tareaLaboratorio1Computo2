#aqui hacemos la importacion de todo lo que vamos a utilizar 
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QMessageBox

class VentanaMascotas(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Datos de las Mascotas")  # aqui va el título de la ventana
        self.setGeometry(100, 100, 400, 400)  # aqui es para colocar el tamaño de la ventana

        layout = QVBoxLayout()  # este es para que el layout sea vertical

        # en esta parte hacemos la lista de datos para las tres mascotas
        self.mascotas = ["Mascota 1", "Mascota 2", "Mascota 3"]
        self.datos_mascotas = ["Nombre", "Especie", "Edad"]
        
        # este es un diccionario para guardar las entradas de las mascotas
        self.entradas_mascotas = {m: {} for m in self.mascotas}

        # aqui creamos la entrada para cada mascota
        for mascota in self.mascotas:
            layout.addWidget(QLabel(mascota, self))
            for dato in self.datos_mascotas:
                layout.addWidget(QLabel(dato + ":", self))  # esta es la etiqueta del dato
                entrada = QLineEdit(self)  # y esta es la entrada de texto
                layout.addWidget(entrada)
                self.entradas_mascotas[mascota][dato] = entrada  # y por ultimo aqui guardamos la entrada

        #este es el boton para enviar y mostrar los datos
        boton_enviar = QPushButton("Ver Los Datos", self)
        boton_enviar.clicked.connect(self.mostrar_datos)
        layout.addWidget(boton_enviar)

        self.setLayout(layout)

    def mostrar_datos(self):
        #esta es para crear un mensaje con los datos ingresados de las 3 mascotas
        mensaje = ""
        for mascota, datos in self.entradas_mascotas.items():
            mensaje += f"{mascota}:\n"
            for dato, entrada in datos.items():
                valor = entrada.text()  #en esta linea de codigo se obtiene el texto ingresado
                mensaje += f"{dato}: {valor}\n"
            mensaje += "\n"

        #en esta parte mostramos los datos ingresados en un mensaje emergente
        QMessageBox.information(self, "Datos Ingresados", mensaje)

app = QApplication(sys.argv)
ventana = VentanaMascotas()
ventana.show()  #y aqui mostramos la ventana
sys.exit(app.exec_())  #aqui inicio el ciclo de eventos