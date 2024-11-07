import pyautogui
import cv2
import numpy as np
import time
import keyboard

screen_width, screen_height = pyautogui.size()

posInicio = 0
posLife = 1
posEndBattle = 2
posNextBattle = 3
posReward = 4 
posAttack = 5

posRecent = -1

scale_factor = 0.4  

region_width = int(screen_width * 0.7) 
region_height = screen_height           

left = 0      
top = 0   

count = 0

templates = {
    "recompensa": cv2.resize(cv2.imread("src/recompensa.png", cv2.IMREAD_GRAYSCALE), None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA),
    "inicio": [
        cv2.resize(cv2.imread("src/inicio.png", cv2.IMREAD_GRAYSCALE), None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA),
        cv2.resize(cv2.imread("src/inicio2.png", cv2.IMREAD_GRAYSCALE), None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)
    ],
    "life": cv2.resize(cv2.imread("src/life.png", cv2.IMREAD_GRAYSCALE), None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA),
    "next_battle": cv2.resize(cv2.imread("src/next_battle.png", cv2.IMREAD_GRAYSCALE), None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA),
    "end_battle": cv2.resize(cv2.imread("src/end_battle.png", cv2.IMREAD_GRAYSCALE), None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA),
}

region = (left, top, region_width, region_height) 
threshold = 0.75  

def detect_windows():
    global posRecent, count
    screenshot = pyautogui.screenshot(region=region)
    screenshot = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    small_screenshot = cv2.resize(screenshot_gray, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)

    # Recorrer cada tipo de ventana y sus plantillas (listas de imágenes o una sola imagen)
    for window_type, templates_list in templates.items():
        # Si templates_list es una lista, iteramos sobre cada imagen en esa lista
        if isinstance(templates_list, list):
            for template in templates_list:
                result = cv2.matchTemplate(small_screenshot, template, cv2.TM_CCOEFF_NORMED)
                loc = np.where(result >= threshold)

                # Si encontramos una coincidencia, ejecutamos la acción para "inicio"
                if len(loc[0]) > 0:
                    if window_type == "inicio":
                        if posRecent == posReward or posRecent == -1 or posRecent == posEndBattle:
                            count = 0
                            posRecent = posInicio
                            keyboard.press_and_release('a')
                            print("Acción: Iniciar juego.")
                    # Salir de la función después de detectar y ejecutar la acción
                    return

        # Si templates_list es una sola imagen, realizamos la detección sin bucle adicional
        else:
            result = cv2.matchTemplate(small_screenshot, templates_list, cv2.TM_CCOEFF_NORMED)
            loc = np.where(result >= threshold)

            if len(loc[0]) > 0:
                # Acciones para otros tipos de ventanas según el tipo detectado
                if window_type == "recompensa":
                    if posRecent == posEndBattle:
                        count = 0
                        posRecent = posReward
                        print("Acción: Recoger recompensa.")
                        time.sleep(0.05)
                        keyboard.press_and_release('esc')
                elif window_type == "life":
                    if posRecent == posInicio:    
                        count = 0
                        posRecent = posLife
                        keyboard.press_and_release('r')
                        time.sleep(0.2)
                        print("Acción: Curar.")
                    elif posRecent == posLife:
                        count = 0
                        posRecent = posAttack
                        keyboard.press_and_release('b')
                        time.sleep(0.2)
                        print("Acción: Atacar.")
                elif window_type == "next_battle":
                    if posRecent == posAttack:
                        count = 0
                        posRecent = posNextBattle
                        print("Acción: siguiente batalla.")
                        keyboard.press_and_release('b')
                elif window_type == "end_battle":
                    if posRecent == posAttack or posRecent == posNextBattle:
                        count = 0
                        posRecent = posEndBattle
                        keyboard.press_and_release('esc')
                        print("Acción: Fin de la batalla.")
                else:
                    print("Ventana desconocida.")
                # Salir de la función después de detectar y ejecutar la acción
                return


while True:
    count += 1
    if count>15:
        time.sleep(0.4)
        keyboard.press_and_release('esc')
        time.sleep(0.4)
        count = 0
        posRecent = -1
        print("Reiniciado")
    detect_windows()
    time.sleep(0.3)