import pyautogui
import keyboard

# Lista para almacenar las posiciones de clic registradas
click_positions = []

def register_clicks():
    print("Modo de registro de clics activado. Presiona 'space' para registrar una posición.")
    print("Presiona 'enter' para finalizar el registro.")
    while True:
        # Detecta si se ha presionado 'space' para registrar la posición actual del mouse
        if keyboard.is_pressed('space'):
            position = pyautogui.position()  # Obtiene la posición actual del cursor
            click_positions.append(position)  # Agrega la posición a la lista
            print(f"Posición registrada: {position}")
            while keyboard.is_pressed('space'):  # Espera a que se suelte 'space'
                pass

        # Detecta si se ha presionado 'enter' para finalizar el registro de posiciones
        if keyboard.is_pressed('enter'):
            print("Registro de posiciones finalizado.")
            print(f"Posiciones guardadas: {click_positions}")
            while keyboard.is_pressed('enter'):  # Espera a que se suelte 'enter'
                pass
            break

def menu():
    print("Bienvenido al menú de configuración")
    print("1. Registrar posiciones de clics")
    print("2. Empezar aplicación")
    option = input("Selecciona una opción (1 o 2): ")
    
    if option == '1':
        register_clicks()
    elif option == '2':
        print("Iniciando la aplicación...")
        # Aquí puedes llamar a la función principal que empieza a capturar screenshots
    else:
        print("Opción no válida. Inténtalo de nuevo.")
        menu()  # Reinicia el menú si la opción no es válida

# Ejecución del menú
menu()

# Ejemplo de uso de las posiciones guardadas en `click_positions`
print("Posiciones de clic guardadas:", click_positions)
# En el código principal puedes hacer clic en esas posiciones de la siguiente forma:
for pos in click_positions:
    pyautogui.click(pos)  # Hace clic en cada posición registrada   