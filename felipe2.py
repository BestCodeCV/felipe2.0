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
    # Realiza clic en la primera posición registrada (simulación)
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
        time.sleep(0.1)  # Simulación de breve pausa entre ataques
        log_message(f"Ataque múltiple en posición: {pos}")

# Función para registrar sectores (simulación)
def registrar_sectores():
    log_message("Modo de registro de sectores. Presiona 'Enter' para guardar la posición.")
    # Cada vez que se presione 'Enter', se agregará la posición actual del cursor
    root.bind('<Return>', save_position)

def save_position(event):
    position = pyautogui.position()  # Obtiene la posición actual del cursor
    click_positions.append(position)  # Agrega la posición a la lista
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

# Función para mostrar mensajes en el cuadro de diálogo
def log_message(message):
    log_text.insert(tk.END, message + "\n")
    log_text.see(tk.END)  # Desplaza el cuadro de texto hacia abajo

# Configuración de la ventana principal
root = tk.Tk()
root.title("Interfaz de Control de Ataque")
root.geometry("300x400")

# Botones principales
button_atacar = tk.Button(root, text="Atacar", command=atacar, width=20)
button_atacar.pack(pady=10)

button_ataque_multiple = tk.Button(root, text="Ataque Múltiple", command=ataque_multiple, width=20)
button_ataque_multiple.pack(pady=10)

button_registrar_sectores = tk.Button(root, text="Registrar Sectores", command=registrar_sectores, width=20)
button_registrar_sectores.pack(pady=10)

# Botones de control (Encender y Stop)
button_encender = tk.Button(root, text="Encender", command=encender_programa, width=10, bg="green")
button_encender.pack(side="left", padx=10, pady=10)

button_stop = tk.Button(root, text="Stop", command=detener_programa, width=10, bg="red")
button_stop.pack(side="right", padx=10, pady=10)

# Cuadro de diálogo para mostrar mensajes
log_text = tk.Text(root, height=10, width=35)
log_text.pack(pady=10)
log_text.insert(tk.END, "Bienvenido al sistema de ataque.\n")

# Inicia el bucle principal de la interfaz gráfica
root.mainloop()
