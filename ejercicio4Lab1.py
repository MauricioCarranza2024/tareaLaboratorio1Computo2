import tkinter as tk
from tkinter import messagebox

# En esta clase llamada mascota, identificamos el nombre, el tipo, la edad de las mascotas que se registraran 
class Mascota:
    def __init__(self, nombre, tipo, edad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad

    def __str__(self):
        return f"Mascota: {self.nombre}, Tipo: {self.tipo}, Edad: {self.edad} años"

# En esta otra clase creamos la venta donde se registraran las mascotas 
class VentanaMascotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Mascotas")
        self.entradas = []

        for i in range(3):
            tk.Label(root, text=f"Mascota {i+1}").grid(row=i*3, column=0, columnspan=2)
            self.crear_entrada(i*3+1, "Nombre:", i)
            self.crear_entrada(i*3+2, "Tipo:", i)
            self.crear_entrada(i*3+3, "Edad:", i)

        tk.Button(root, text="Registrar Mascotas", command=self.leer_datos).grid(row=10, column=0, columnspan=2)

    def crear_entrada(self, fila, texto, indice):
        tk.Label(self.root, text=texto).grid(row=fila, column=0)
        entrada = tk.Entry(self.root)
        entrada.grid(row=fila, column=1)
        if len(self.entradas) <= indice:
            self.entradas.append([None, None, None])
        self.entradas[indice][fila%3] = entrada

    def leer_datos(self):
        mascotas = []
        for entrada in self.entradas:
            nombre, tipo, edad = entrada[0].get(), entrada[1].get(), entrada[2].get()
            try:
                mascotas.append(Mascota(nombre, tipo, int(edad)))
            except ValueError:
                messagebox.showerror("Error", "La edad debe ser un número entero.")
                return
        info = "\n".join(str(mascota) for mascota in mascotas)
        messagebox.showinfo("Mascotas Registradas", info)

# y por ultimo donde se ejecutara el programa de registro de mascotas 
if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaMascotas(root)
    root.mainloop()

