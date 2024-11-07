import pyautogui
import cv2
import numpy as np
import time
import keyboard

screen_width, screen_height = pyautogui.size()


# Definición de los estados posibles
posInicio = 0
posLife = 1
posEndBattle = 2
posNextBattle = 3
posReward = 4 
posAttack = 5

# Variable para almacenar el estado reciente
posRecent = -1

# Factor de escala para optimizar la velocidad
scale_factor = 0.4  # Escalar al 50%

# Define el tamaño de la región de captura
region_width = int(screen_width * 0.7)  # 50% del ancho
region_height = screen_height           # 100% del alto

# Calcula las coordenadas para centrar la región en la pantalla, desplazada un poco a la izquierda
left = 0      # Comienza el borde izquierdo un poco a la izquierda del centro
top = 0   

# Cargar y escalar plantillas una vez al inicio
templates = {
    "recompensa": cv2.resize(cv2.imread("src/recompensa.png", cv2.IMREAD_GRAYSCALE), None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA),
    "inicio": cv2.resize(cv2.imread("src/inicio.png", cv2.IMREAD_GRAYSCALE), None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA),
    "life": cv2.resize(cv2.imread("src/life.png", cv2.IMREAD_GRAYSCALE), None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA),
    "next_battle": cv2.resize(cv2.imread("src/next_battle.png", cv2.IMREAD_GRAYSCALE), None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA),
    "end_battle": cv2.resize(cv2.imread("src/end_battle.png", cv2.IMREAD_GRAYSCALE), None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA),
}

# Coordenadas para capturar solo una región específica de la pantalla
region = (left, top, region_width, region_height)  # Ajusta estas coordenadas según el área de interés
threshold = 0.75  # Nivel de coincidencia optimizado

def detect_windows():
    global posRecent 
    screenshot = pyautogui.screenshot(region=region)
    screenshot = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    small_screenshot = cv2.resize(screenshot_gray, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)

    for window_type, template in templates.items():
        result = cv2.matchTemplate(small_screenshot, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)
        curado = 0
        if len(loc[0]) > 0:
            #print(f"Ventana '{window_type}' detectada")
            # If-else para tomar acción en base al tipo de ventana detectada
            if window_type == "recompensa":
                if posRecent == posEndBattle:
                    posRecent = posReward
                    print("Acción: Recoger recompensa.")
                    time.sleep(250 / 1000)
                    keyboard.press_and_release('esc')
            # Aquí puedes definir la acción para la ventana de recompensa
            elif window_type == "inicio":
                if posRecent == posReward or posRecent == -1 or posRecent == posEndBattle:
                    posRecent = posInicio
                    keyboard.press_and_release('a')
                    print("Acción: Iniciar juego.")
            # Acción para la ventana de inicio
            elif window_type == "life":
                if posRecent == posInicio:    
                    posRecent = posLife
                    keyboard.press_and_release('r')
                    time.sleep(200 / 1000)
                    print("Acción: Curar.")
                elif posRecent == posLife:
                    posRecent = posAttack
                    keyboard.press_and_release('b')
                    time.sleep(200 / 1000)
                    print("Acción: Atacar.")
            # Acción para la ventana de vida
            elif window_type == "next_battle":
                if posRecent == posAttack:
                    posRecent = posNextBattle
                    print("Acción: siguiente batalla.")
                    keyboard.press_and_release('b')
            # Acción para la ventana de próxima batalla
            elif window_type == "end_battle":
                if posRecent == posAttack or posRecent == posNextBattle:
                    posRecent = posEndBattle
                    keyboard.press_and_release('esc')
                    print("Acción: Fin de la batalla.")
            # Acción para la ventana de fin de batalla
            else:
                print("Ventana desconocida.")
            # Salir de la función después de detectar una ventana y ejecutar la acción
            return

# Bucle principal
while True:
    detect_windows()
    time.sleep(0.3)
