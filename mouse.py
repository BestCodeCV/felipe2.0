import pyautogui
import time

print("Haz clic derecho para obtener la posición del mouse. Presiona Ctrl+C para salir.")

clics_guardados = [(314, 420), (143, 305), (722, 460)] 

try:
    while True:
        if pyautogui.mouseInfo() == 'right':
            x, y = pyautogui.position()  # Obtiene la posición actual del cursor
            print(f"Clic derecho detectado en las coordenadas: ({x}, {y})")
            time.sleep(0.5)  # Evita que imprima múltiples veces por un solo clic
except KeyboardInterrupt:
    print("\nPrograma finalizado.")