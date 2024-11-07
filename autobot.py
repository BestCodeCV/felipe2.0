import pyautogui
import cv2
import numpy as np
import time
import keyboard

posInicio = 0
posLife = 1
posEndBattle = 2
posNextBattle = 3
posReward = 4 

posRecent = -1

templates = {
    "recompensa": cv2.imread("src/recompensa.png", cv2.IMREAD_GRAYSCALE),
    "inicio": cv2.imread("src/inicio.png", cv2.IMREAD_GRAYSCALE),
    "life": cv2.imread("src/life.png", cv2.IMREAD_GRAYSCALE),
    "next_battle": cv2.imread("src/next_battle.png", cv2.IMREAD_GRAYSCALE),
    "end_battle": cv2.imread("src/end_battle.png", cv2.IMREAD_GRAYSCALE),
}

threshold = 0.7

def detect_windows():
    global posRecent 
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    for window_type, template in templates.items():
        w, h = template.shape[::-1]
        
        result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)

        if len(loc[0]) > 0:
            #print(f"Ventana '{window_type}' detectada")
            # If-else para tomar acción en base al tipo de ventana detectada
            if window_type == "recompensa":
                if posRecent == posEndBattle:
                    posRecent = posReward
                    keyboard.press_and_release('esc')
                    print("Acción: Recoger recompensa.")
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
                    time.sleep(500 / 1000)
                    keyboard.press_and_release('b')
                    print("Acción: Curar.")
            # Acción para la ventana de vida
            elif window_type == "next_battle":
                if posRecent == posLife:
                    posRecent = posNextBattle
                    keyboard.press_and_release('b')
                    print("Acción: siguiente batalla.")
            # Acción para la ventana de próxima batalla
            elif window_type == "end_battle":
                if posRecent == posLife or posRecent == posNextBattle:
                    posRecent = posEndBattle
                    keyboard.press_and_release('esc')
                    print("Acción: Fin de la batalla.")
            # Acción para la ventana de fin de batalla
            else:
                print("Ventana desconocida.")
            # Salir de la función después de detectar una ventana y ejecutar la acción
            return
while True:
    detect_windows()
    time.sleep(0.25)  # Espera un segundo antes de la siguiente comprobación