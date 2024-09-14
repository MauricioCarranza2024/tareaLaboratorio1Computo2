import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout

class PersonaForm(QWidget):
    def _init_(self):
        super()._init_()

        # Configuración de la ventana
        self.setWindowTitle("Datos de la Persona")
        self.setGeometry(100, 100, 400, 500)

        # diseño y los widgets
        layout = QGridLayout()

        # Lista de los datos de usuario
        datos = [
            "Nombre", "Edad", "Género", "Dirección", "Teléfono",
            "Correo Electrónico", "Ocupación", "Estado Civil",
            "Nacionalidad", "Fecha de Nacimiento"
        ]

        # elaborar campos de entrada para cada dato
        self.campos = {}
        for i, dato in enumerate(datos):
            label = QLabel(f"{dato}:")
            input_field = QLineEdit()

            # Añadir al layout
            layout.addWidget(label, i, 0)
            layout.addWidget(input_field, i, 1)

            # Almacenar el campo de entrada 
            self.campos[dato] = input_field

        # Botón para imprimir los datos
        self.print_button = QPushButton("Imprimir Datos")
        self.print_button.clicked.connect(self.print_data)

        # Aplicar estilo al botón para cambiar el color azul
        self.print_button.setStyleSheet("background-color: blue; color: white; font-weight: bold;")

        layout.addWidget(self.print_button, len(datos), 0, 1, 2)

        # Botón de resetear rojo
        self.reset_button = QPushButton("Resetear")
        self.reset_button.clicked.connect(self.reset_fields)
        self.reset_button.setStyleSheet("background-color: red; color: white; font-weight: bold;")

        layout.addWidget(self.reset_button, len(datos) + 1, 0, 1, 2)

        # volver al diseño principal
        self.setLayout(layout)

    def print_data(self):
        # Obtener y mostrar los datos de la persona
        print("Datos de la Persona:")
        print("--------------------")
        for key, input_field in self.campos.items():
            value = input_field.text()
            print(f"{key}: {value}")
        print("--------------------")

    def reset_fields(self):
        # Resetear todos los campos de entrada
        for input_field in self.campos.values():
            input_field.clear()

# Crear la aplicación
app = QApplication(sys.argv)
window = PersonaForm()
window.show()
sys.exit(app.exec_())