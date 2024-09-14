#aqui hacemos la importacion de todo lo que vamos a utilizar
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt  # aqui importe Qt ya que es necesario para alinear al centro

class VentanaNombreEdad(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nombre y Edad")  # Aqui escribi el titulo de como se llamara mi ventana
        self.setGeometry(100, 100, 400, 200)  # aqui puse el tamaño de la ventana que necesito
        
        layout = QVBoxLayout()  # Usamos un layout vertical

        # Esta es la etiqueta para mostrar el nombre, 
        # el cual puse el mio y el de mi compañero 
        nombre = QLabel("Nombre: Mauricio Carranza, Erick Chavez", self)
        nombre.setAlignment(Qt.AlignCenter)  # Alineación al centro
        
        # Esta es la etiqueta para mostrar la edad, 
        # la cual puse mi edad y la de mi compañero como simulacion
        edad = QLabel("Edad: 18 y 19 años", self)
        edad.setAlignment(Qt.AlignCenter)  # Aqui usamos una alineación al centro

        # en esta parte agregarmos los widgets al layout
        layout.addWidget(nombre)
        layout.addWidget(edad)
        
        self.setLayout(layout)  # Aqui asigne el layout a la ventana

app = QApplication(sys.argv)
ventana = VentanaNombreEdad()
ventana.show()  # posteriormente muesto la ventana
sys.exit(app.exec_())  # Inicio el ciclo de eventos
