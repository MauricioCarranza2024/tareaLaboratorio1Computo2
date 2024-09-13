import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, QRadioButton, QComboBox, QSpinBox, QPushButton, QMessageBox

class VentanaWidgets(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio con PyQt5")  # aqui va el título de la ventana
        self.setGeometry(100, 100, 400, 300)  # aqui va el tamaño de la ventana

        layout = QVBoxLayout()  # este es para que el layout sea vertical

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
        self.spin_edad.setRange(0, 100)  # aqui le puse que la edad tenga un ango de 0 a 100 años

        # aqui coloque un botón para enviar los datos
        self.boton_enviar = QPushButton("Enviar", self)
        self.boton_enviar.clicked.connect(self.enviar_datos)

        # aqui agregamos el widgets al layout
        layout.addWidget(self.label_genero)
        layout.addWidget(self.radio_masculino)
        layout.addWidget(self.radio_femenino)
        layout.addWidget(self.label_pais)
        layout.addWidget(self.combo_pais)
        layout.addWidget(self.label_edad)
        layout.addWidget(self.spin_edad)
        layout.addWidget(self.boton_enviar)

        self.setLayout(layout)

    def enviar_datos(self):
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
        QMessageBox.information(self, "Datos ingresados", f"Género: {genero}\nPaís: {pais}\nEdad: {edad}")

app = QApplication(sys.argv)
ventana = VentanaWidgets()
ventana.show()  # Por ultimo mostramos la ventana
sys.exit(app.exec_())  # Inicio el ciclo de eventos
