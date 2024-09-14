#aqui hacemos la importacion de todo lo que vamos a utilizar
import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QRadioButton, QComboBox, QSpinBox, QPushButton, QMessageBox, QLineEdit

class VentanaWidgets(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulario de Datos Personales")  # aqui va el título de la ventana
        self.setGeometry(100, 100, 400, 350)  # aqui va el tamaño de la ventana

        layout = QVBoxLayout()  # este es para que el layout sea vertical

        # Aqui se agregó un campo de texto para el nombre
        self.label_nombre = QLabel("Ingrese su nombre:", self)
        self.input_nombre = QLineEdit(self)

        # Aqui use RadioButton para poder seleccionar el género
        self.label_genero = QLabel("Seleccione su género:", self)
        self.radio_masculino = QRadioButton("Masculino", self)
        self.radio_femenino = QRadioButton("Femenino", self)

        # Aqui use ComboBox para poder seleccionar un país
        self.label_pais = QLabel("Seleccione su país:", self)
        self.combo_pais = QComboBox(self)
        self.combo_pais.addItems(["El Salvador", "Guatemala", "Honduras", "Costa Rica", "Panamá"])

        # Aqui use SpinBox para seleccionar la edad
        self.label_edad = QLabel("Seleccione su edad:", self)
        self.spin_edad = QSpinBox(self)
        self.spin_edad.setRange(0, 100)  # aqui le puse que la edad tenga un rango de 0 a 100 años

        # aqui coloque un boton para ver los datos enviados los datos
        self.boton_ver = QPushButton("Ver datos", self)
        self.boton_ver.clicked.connect(self.enviar_datos)

        # aqui agregamos el widgets al layout
        layout.addWidget(self.label_nombre)
        layout.addWidget(self.input_nombre)
        layout.addWidget(self.label_genero)
        layout.addWidget(self.radio_masculino)
        layout.addWidget(self.radio_femenino)
        layout.addWidget(self.label_pais)
        layout.addWidget(self.combo_pais)
        layout.addWidget(self.label_edad)
        layout.addWidget(self.spin_edad)
        layout.addWidget(self.boton_ver)

        self.setLayout(layout)

    def enviar_datos(self):
        # Aqui obtenemos el nombre ingresado
        nombre = self.input_nombre.text()

        # usamos el if para obtener el género seleccionado
        if self.radio_masculino.isChecked():
            genero = "Masculino"
        elif self.radio_femenino.isChecked():
            genero = "Femenino"
        else:
            genero = "No especificado"

        # tambien aqui para obtener el país seleccionado
        pais = self.combo_pais.currentText()

        # y aqui para obtener la edad seleccionada
        edad = self.spin_edad.value()

        # Aqui mostramos los datos seleccionados en un mensaje emergente
        QMessageBox.information(self, "Datos ingresados", f"Nombre: {nombre}\nGénero: {genero}\nPaís: {pais}\nEdad: {edad} años")

app = QApplication(sys.argv)
ventana = VentanaWidgets()
ventana.show()  # Por ultimo mostramos la ventana
sys.exit(app.exec_())  # Inicio el ciclo de eventos
