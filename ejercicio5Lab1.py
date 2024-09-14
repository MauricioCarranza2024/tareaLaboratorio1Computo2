import tkinter as tk
from tkinter import messagebox

# Aca hacemos la creacion de la clase persona para solicitar los datos al usuario de se va registrar 
class Persona:
    def __init__(self, nombre, apellido, edad, direccion, telefono, email, ocupacion, genero, estado_civil, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.ocupacion = ocupacion
        self.genero = genero
        self.estado_civil = estado_civil
        self.nacionalidad = nacionalidad

    def __str__(self):
        return (f"Nombre: {self.nombre} {self.apellido}\nEdad: {self.edad}\nDirección: {self.direccion}\n"
                f"Teléfono: {self.telefono}\nEmail: {self.email}\nOcupación: {self.ocupacion}\n"
                f"Género: {self.genero}\nEstado Civil: {self.estado_civil}\nNacionalidad: {self.nacionalidad}")

# En esta otra clase habilitamos la ventana para que la persona se registre 
class VentanaPersona:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Persona")
        self.root.configure(bg="#f0f0f0")
        self.datos = ["Nombre", "Apellido", "Edad", "Dirección", "Teléfono", "Email", "Ocupación", "Género", "Estado Civil", "Nacionalidad"]
        self.entradas = []

        # aca creamos el titulo de la venta que seria la interfas de el progrma 
        titulo = tk.Label(root, text="Formulario de Registro de Persona", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
        titulo.grid(row=0, column=0, columnspan=2, pady=(10, 20))

        # aca es donde se crean las etiquetas y entrada para obtener los 10 datos
        for i, dato in enumerate(self.datos):
            tk.Label(root, text=dato + ":", font=("Arial", 12), bg="#f0f0f0", fg="#333").grid(row=i+1, column=0, padx=(10, 10), pady=(5, 5), sticky="e")
            entrada = tk.Entry(root, font=("Arial", 12), width=30)
            entrada.grid(row=i+1, column=1, padx=(10, 10), pady=(5, 5))
            self.entradas.append(entrada)

        # esta es la creacion del boton para registrar los datos de las personas 
        boton_registrar = tk.Button(root, text="Registrar Persona", command=self.leer_datos, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
        boton_registrar.grid(row=11, column=0, columnspan=2, pady=(20, 10))

        # y este es el boton para salir del programa
        boton_salir = tk.Button(root, text="Salir", command=self.salir, font=("Arial", 12), bg="#F44336", fg="white", padx=10, pady=5)
        boton_salir.grid(row=12, column=0, columnspan=2, pady=(10, 10))

    def leer_datos(self):
        try:
            datos_persona = [entrada.get() for entrada in self.entradas]
            persona = Persona(*datos_persona[:2], int(datos_persona[2]), *datos_persona[3:])
            messagebox.showinfo("Datos Registrados", str(persona))
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número entero.")
    
    def salir(self):
        self.root.quit()

# y aca se ejecuta el programa 
if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPersona(root)
    root.mainloop()
