import tkinter as tk
from tkinter import scrolledtext, font
import threading
import sys
from io import StringIO

import main

class Redirector:
    def __init__(self, widget):
        self.widget = widget

    def write(self, text_str):
        self.widget.after(0, self.insert_text, text_str)

    def insert_text(self, text_str):
        self.widget.config(state="normal")
        self.widget.insert(tk.END, text_str)
        self.widget.see(tk.END)
        self.widget.config(state="disabled")

def ejecutar_logica(expresion):
    output_text.after(0, lambda: output_text.config(state="normal"))
    output_text.after(0, lambda: output_text.delete("1.0", tk.END))
    output_text.after(0, lambda: output_text.config(state="disabled"))
    
    original_stdout = sys.stdout
    original_stdin = sys.stdin

    try:
        entrada_simulada = f"{expresion}\ns\n"
        sys.stdin = StringIO(entrada_simulada)
        sys.stdout = Redirector(output_text)
        main.menu()

    except Exception as e:
        sys.stdout.write(f"\nERROR\n{e}")
    finally:
        sys.stdout = original_stdout
        sys.stdin = original_stdin

def iniciar():
    #Función al presionar el botón "Generar".
    expresion_ingresada = entry_expresion.get()
    if not expresion_ingresada.strip():
        output_text.config(state="normal")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Error: Por favor ingrese una expresión.")
        output_text.config(state="disabled")
        return
    
    hilo = threading.Thread(target=ejecutar_logica, args=(expresion_ingresada,))
    hilo.start()

#Configuración de la ventana principal
root = tk.Tk()
root.title("Generador de Tablas de Verdad")
root.geometry("720x600")

input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=10, fill="x")

label_instruccion = tk.Label(input_frame, text="Expresión Lógica (&&, ||, !, ->, <->):", font=("Arial", 20))
label_instruccion.pack(side="left", padx=(0, 5))

entry_expresion = tk.Entry(input_frame, width=40, font=("Arial", 20))
entry_expresion.pack(side="left", fill="x", expand=True)
entry_expresion.bind("<Return>", lambda event: iniciar())

boton_generar = tk.Button(input_frame, text="Generar Tabla", command=iniciar)
boton_generar.pack(side="left", padx=(5, 0))

output_frame = tk.Frame(root)
output_frame.pack(padx=10, pady=(0, 10), fill="both", expand=True)

output_text = scrolledtext.ScrolledText(output_frame, wrap="none", state="disabled", bg="#2b2b2b", fg="#f8f8f2")
output_text.pack(fill="both", expand=True)

mono_font = font.Font(family="Courier New", size=20)
output_text.configure(font=mono_font)

if __name__ == '__main__':
    root.mainloop()