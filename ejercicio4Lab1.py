import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout

class MascotaForm(QWidget):
    def _init_(self):
        super()._init_()

        # Configuración de la ventana
        self.setWindowTitle("Datos de Mascotas")
        self.setGeometry(100, 100, 400, 300)

        # Crear el diseño y los widgets
        layout = QGridLayout()

        # Crear etiquetas y campos de entrada para cada mascota
        self.mascotas = []
        for i in range(3):
            nombre_label = QLabel(f"Mascota {i + 1} Nombre:")
            edad_label = QLabel(f"Mascota {i + 1} Edad:")
            tipo_label = QLabel(f"Mascota {i + 1} Tipo:")

            nombre_input = QLineEdit()
            edad_input = QLineEdit()
            tipo_input = QLineEdit()

            # Añadir al layout
            layout.addWidget(nombre_label, i * 3, 0)
            layout.addWidget(nombre_input, i * 3, 1)
            layout.addWidget(edad_label, i * 3 + 1, 0)
            layout.addWidget(edad_input, i * 3 + 1, 1)
            layout.addWidget(tipo_label, i * 3 + 2, 0)
            layout.addWidget(tipo_input, i * 3 + 2, 1)

            # Almacenar los campos de entrada para acceder a ellos despues
            self.mascotas.append({
                'nombre': nombre_input,
                'edad': edad_input,
                'tipo': tipo_input
            })

        # este boton imprime los datos
        self.print_button = QPushButton("Imprimir Datos")
        self.print_button.clicked.connect(self.print_data)
        layout.addWidget(self.print_button, 9, 0, 1, 2)

        # regresar al diseño principal
        self.setLayout(layout)

    def print_data(self):
        # Obtener y mostrar los datos de cada mascota
        for i, mascota in enumerate(self.mascotas):
            nombre = mascota['nombre'].text()
            edad = mascota['edad'].text()
            tipo = mascota['tipo'].text()
            print(f"Mascota {i + 1}:")
            print(f"  Nombre: {nombre}")
            print(f"  Edad: {edad}")
            print(f"  Tipo: {tipo}")
            print("--------------------")

# Crear la aplicación
app = QApplication(sys.argv)
window = MascotaForm()
window.show()
sys.exit(app.exec_())

