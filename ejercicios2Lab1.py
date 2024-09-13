import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox

class VentanaClaveSecreta(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ingresar Clave Secreta")  #  aqui va el título de la ventana
        self.setGeometry(100, 100, 400, 150)  # aqui es para colocar el tamaño de la ventana

        layout = QVBoxLayout()  #este es para que el layout sea vertical

        # aqui puse una etiqueta y campo de texto para la clave secreta
        self.label_clave = QLabel("Ingrese su clave secreta:", self)
        self.input_clave = QLineEdit(self)
        self.input_clave.setEchoMode(QLineEdit.Password)  # Ocultar los caracteres ingresados

        #aqui puse un boton para enviar los datos
        self.boton_enviar = QPushButton("Enviar", self)
        self.boton_enviar.clicked.connect(self.enviar_datos)

        # aqui añadi los widgets al layout
        layout.addWidget(self.label_clave)
        layout.addWidget(self.input_clave)
        layout.addWidget(self.boton_enviar)

        self.setLayout(layout)

    def enviar_datos(self):
        # en esta parte la hice para obtener la clave secreta ingresada
        clave = self.input_clave.text()

        # aqui mostre la clave en un mensaje emergente (para demostración)
        QMessageBox.information(self, "Clave Ingresada", "Clave ingresada correctamente.")

app = QApplication(sys.argv)
ventana = VentanaClaveSecreta()
ventana.show()  # por ultimo muestro la ventana
sys.exit(app.exec_())  # y inicio el ciclo de eventos
