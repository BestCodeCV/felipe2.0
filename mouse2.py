import pyautogui
import time
import keyboard

print("Haz clic derecho para obtener la posición del mouse. Presiona Ctrl+C para salir.")

clics_guardados = [(314, 420), (143, 305), (722, 460)] 
index_clic_actual = 0
count = 0

while True:
    count += 1
    
    if count > 15:
        time.sleep(0.4)
        keyboard.press_and_release('esc')
        time.sleep(0.4)
        count = 0
        posRecent = -1
        print("Reiniciado")
        
        # Verifica que el índice actual esté dentro del rango de la lista de coordenadas
        if index_clic_actual < len(clics_guardados):
            # Obtiene las coordenadas para el clic
            x, y = clics_guardados[index_clic_actual]
            
            # Realiza el clic en las coordenadas especificadas
            pyautogui.click(x, y)
            print(f"Se hizo clic en las coordenadas: {x}, {y}")
            
            # Avanza al siguiente clic en la lista
            index_clic_actual += 1
        

    #detect_windows()
    time.sleep(0.3)