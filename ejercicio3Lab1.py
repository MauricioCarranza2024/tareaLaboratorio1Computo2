#aqui hacemos la importacion de todo lo que vamos a utilizar
import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox

class VentanaCedulaNombre(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Leer Cédula y Nombre Completo")  # aqui va el título de la ventana
        self.setGeometry(100, 100, 400, 200)  # aqui es para colocar el tamaño de la ventana

        layout = QVBoxLayout()  # este es para que el layout sea vertical

        # aqui coloque la etiqueta y campo de texto para el número de cédula
        self.label_cedula = QLabel("Ingrese su número de cédula:", self)
        self.input_cedula = QLineEdit(self)

        # aqui coloque tiqueta y campo de texto para el nombre completo
        self.label_nombre = QLabel("Ingrese su nombre completo:", self)
        self.input_nombre = QLineEdit(self)

        # aqui puse un boton para enviar los datos
        self.boton_enviar = QPushButton("Ver completamente", self)
        self.boton_enviar.clicked.connect(self.enviar_datos)

        # en esta parte añadi los widgets al layout
        layout.addWidget(self.label_cedula)
        layout.addWidget(self.input_cedula)
        layout.addWidget(self.label_nombre)
        layout.addWidget(self.input_nombre)
        layout.addWidget(self.boton_enviar)

        self.setLayout(layout)

    def enviar_datos(self):
        # este es para obtener el número de cédula y el nombre ingresados
        cedula = self.input_cedula.text()
        nombre = self.input_nombre.text()

        # este es para mostrar los datos en un mensaje emergente
        QMessageBox.information(self, "Datos Ingresados", f"Cédula: {cedula}\nNombre: {nombre}")

app = QApplication(sys.argv)
ventana = VentanaCedulaNombre()
ventana.show()  # aqui muestro la ventana
sys.exit(app.exec_())  # Inicio el ciclo de eventos
