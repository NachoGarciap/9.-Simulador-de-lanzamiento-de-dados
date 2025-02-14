from farkle import Farkle
from lanzador_dados import LanzarDado
from mafia import Mafia
from reglas_juegos import Reglas_juego
from suma_exacta import SumaExacta

reglas = Reglas_juego()
juego_farkle = Farkle()
juego_lanzar_dados = LanzarDado()
juego_mafia = Mafia()
juego_suma_exacta = SumaExacta()


while True:
    print('🎲🎲----- Juegos de dados -----🎲🎲')
    print('1. Farkle')
    print('2. Lanzar Dados')
    print('3. Mafia')
    print('4. Suma Exacta')
    print('5. Salir')

    try:
        opcion = int(input("Elige un modo de juego: "))
    except ValueError:
        print("❌ Entrada no válida. Ingresa un número del 1 al 4.")
        continue  # Vuelve a mostrar el menú

    if opcion == 1:
        juego_farkle.mostrar_menu()
    elif opcion == 2:
        juego_lanzar_dados.mostrar_menu()
    elif opcion == 3:
        juego_mafia.mostrar_menu()
    elif opcion == 4:
        juego_suma_exacta.mostrar_menu()
    elif opcion == 5:
        print('Saliendo del juego...')
        break
    else:
        print('Introduce un juego valido!')
