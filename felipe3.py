import tkinter as tk
from tkinter import messagebox
import pyautogui
import time

# Lista para almacenar posiciones registradas
click_positions = []
program_running = False  # Variable de control para iniciar y detener el programa

# Función para atacar en una posición
def atacar():
    if not click_positions:
        log_message("No hay sectores registrados para atacar.")
        return
    for pos in click_positions:
        pyautogui.click(pos)
        log_message(f"Sector atacado en posición: {pos}")

# Función para un ataque múltiple
def ataque_multiple():
    if not click_positions:
        log_message("No hay sectores registrados para ataque múltiple.")
        return
    for pos in click_positions:
        pyautogui.click(pos)
        time.sleep(0.1)  
        log_message(f"Ataque múltiple en posición: {pos}")

# Función para registrar sectores (simulación)
def registrar_sectores():
    log_message("Modo de registro de sectores. Presiona 'Enter' para guardar la posición.")
    root.bind('<Return>', save_position)

def save_position(event):
    position = pyautogui.position()
    click_positions.append(position)
    log_message(f"Posición registrada: {position}")

# Función para encender el programa
def encender_programa():
    global program_running
    program_running = True
    log_message("Programa encendido")

# Función para detener el programa
def detener_programa():
    global program_running
    program_running = False
    log_message("Programa detenido")

# Función para mostrar un solo mensaje en el cuadro de diálogo
def log_message(message):
    log_text.config(state=tk.NORMAL)  # Habilita la edición temporalmente
    log_text.delete(1.0, tk.END)  # Borra el mensaje anterior
    log_text.insert(tk.END, message)  # Inserta el nuevo mensaje
    log_text.config(state=tk.DISABLED)  # Deshabilita la edición nuevamente

# Configuración de la ventana principal
root = tk.Tk()
root.title("Felipe 2.0")
root.geometry("260x300")
root.configure(bg="#2d2d2d")  # Fondo oscuro de la ventana principal

# Cuadro de diálogo para mostrar mensajes (en la parte superior)
log_text = tk.Text(root, height=3, width=35, bg="#3e3e3e", fg="#ffffff", font=("Roboto", 9, "normal"))
log_text.pack(pady=(10, 15))  # Separación del borde superior
log_text.insert(tk.END, "Bienvenido al sistema de ataque.")
log_text.config(state=tk.DISABLED)

# Estilos de botones
button_style = {"bg": "#4a4a4a", "fg": "#ffffff", "font": ("Roboto", 10, "normal"), "width": 15, "height": 1, "pady": 5}

# Botones principales
button_atacar = tk.Button(root, text="Atacar", command=atacar, **button_style)
button_atacar.pack(pady=5)

button_ataque_multiple = tk.Button(root, text="Ataque Múltiple", command=ataque_multiple, **button_style)
button_ataque_multiple.pack(pady=5)

button_registrar_sectores = tk.Button(root, text="Registrar Sectores", command=registrar_sectores, **button_style)
button_registrar_sectores.pack(pady=5)

# Estilos de botones pequeños
small_button_style = {"width": 10, "height": 1, "font": ("Roboto", 9, "normal")}

# Botones de control (Encender y Stop)
button_encender = tk.Button(root, text="Encender", command=encender_programa, bg="#2ecc71", fg="#ffffff", **small_button_style)
button_encender.pack(side="left", padx=10, pady=10)

button_stop = tk.Button(root, text="Stop", command=detener_programa, bg="#e74c3c", fg="#ffffff", **small_button_style)
button_stop.pack(side="right", padx=10, pady=10)

# Inicia el bucle principal de la interfaz gráfica
root.mainloop()
