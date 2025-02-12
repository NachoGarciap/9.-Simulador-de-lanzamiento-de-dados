from farkle import Farkle
from reglas_juegos import Reglas_juego

reglas = Reglas_juego()
juego = Farkle()


while True:
    print('🎲🎲----- Juegos de dados -----🎲🎲')
    print('1. Farkle, reglas del juego')
    print('2. Jugar Farkle')
    print('3. Lanzar dados')
    print('4. Salir del juego')

    try:
        opcion = int(input("Elige un modo de juego: "))
    except ValueError:
        print("❌ Entrada no válida. Ingresa un número del 1 al 4.")
        continue  # Vuelve a mostrar el menú

    if opcion == 1:
        reglas.reglas_farkle()
    elif opcion == 2:
        juego.calcular_puntos()
    elif opcion == 3:
        pass
    elif opcion == 4:
        print('Saliendo del juego...')
        break
    else:
        print('Introduce un juego valido!')
