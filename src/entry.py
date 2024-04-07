import os
from .process.errorFilter import errorFilter

# Función para limpiar la pantalla de la terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Ciclo infinito para mantener la calculadora en ejecución
def entryLoop():
    print('Bienvenidos!\n')

    while True:
        userInput = input('calculadora>> ')

        if userInput == 'quit':
            print('\nSaliendo de la calculadora. ¡Hasta luego!\n')
            break

        if userInput == 'clear':
            clear_screen()
            continue

        # Procesamiento de la entrada del usuario para la veficación de errores
        errorFilter(userInput)