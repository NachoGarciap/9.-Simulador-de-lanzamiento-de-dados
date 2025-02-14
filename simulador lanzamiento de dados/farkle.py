import random
import time

from reglas_juegos import Reglas_juego


class Farkle:

    def __init__(self):
        print('🎲----- Bienvenidos al juego Farkle -----🎲')
        self.dado = [1, 2, 3, 4, 5, 6]
        self.max_puntuacion = 1000
        # self.puntos_totales = 0
        # Puntos de lso jugadores
        self.puntos_jugador1 = 0
        self.puntos_jugador2 = 0
        # Turnos de los jugadores turno 1 = jugador 1
        self.turno = 1

    def mostrar_menu(self):
        while True:
            print('🎲----- Farkle -----🎲')
            print('1. Reglas')
            print('2. Jugar')
            print('3. Salir')

            try:
                opcion = int(input("Elige un modo de juego: "))
            except ValueError:
                print('Introduce una opcion valida, por favor.')
                continue #asi vuelve a iniciar el try hasta que la opcion sea correcta

            if opcion == 1:
                print('----- Recordatorio de las reglas y los puntos! -----')
                reglas.reglas_farkle()
            elif opcion == 2:
                print('----- Empieza la partida! -----')
                self.jugar()
            elif opcion == 3:
                print('Saliendo del juego...')
                break
            else:
                print('Introduce una opcion valida')

    def lanzar_dado(self, cantidad=6):  # lanza los dados y devuelve una lista con los resultados

        print('Lanzamos los dados...🎲🎲')
        time.sleep(2)

        resultados = []
        for _ in range(cantidad):
            resultado = random.choice(self.dado)
            resultados.append(resultado)
        print(f"Han salido {cantidad} dados, con estos resultados: {resultados}")
        print('____________________________________')
        return resultados

    def calcular_puntos(self):
        dados_lanzados = self.lanzar_dado()
        print('Contamos los puntos que han salido...🎲🎲')
        time.sleep(2)

        puntos_ronda = 0

        # Contar ocurrencias de cada número
        contador = {}
        for dado in set(dados_lanzados):  # con el set, quitamos los duplicados
            contador[dado] = dados_lanzados.count(dado)  # Contamos las veces que aparece
        print(f'Contador de números: {contador}')

        print('____________________________________')

        # Reglas puntuación
        for valor, cantidad in contador.items():  # ejemplo: {1: 1, 2: 1, 3: 1, 5: 1, 6: 2}
            # Si hay al menos 3 del mismo número, se cuentan como un trío
            if cantidad >= 3:
                if valor == 1:
                    puntos_ronda += 300  # tres unos = 300 puntos
                else:
                    puntos_ronda += valor * 100  # Trio de cualquier otro número, ejemplo 3*100= 300 puntos
                cantidad -= 3  # Quitamos los 3 dados ya puntuados

            # Dados extra 1=100puntos 5=50puntos
            if valor == 1:
                puntos_ronda += cantidad * 100  # Cada 1 suma 100 puntos
            elif valor == 5:
                puntos_ronda += cantidad * 50  # Cada 5 suma 50 puntos

        # Comprobamos si hay una escalera (de 1 al 6)
        print('Comprobando si hay escalera...🎲🎲')
        time.sleep(2)
        if set(dados_lanzados) == {1, 2, 3, 4, 5, 6}:  # con el set, quitamos los duplicados
            puntos_ronda += 1500  # escalera completa
            print("¡Escalera completa! 1500 puntos.")
        else:
            print('No hay escalera!')

        print('____________________________________')
        print(f'Total puntos conseguidos: {puntos_ronda}')
        print('____________________________________')
        return puntos_ronda

    def jugar(self):
        while self.puntos_jugador1 < self.max_puntuacion and self.puntos_jugador2 < self.max_puntuacion:
            print(f"\nTurno del Jugador {self.turno}")
            if self.turno == 1:
                print(f'Puntos totales jugador 1: {self.puntos_jugador1}')
            else:
                print(f'Puntos totales jugador 2: {self.puntos_jugador2}')

            puntos_ronda = self.calcular_puntos()  # Juega el turno actual

            # Diferentes turnos de los jugadores
            if self.turno == 1:
                self.puntos_jugador1 += puntos_ronda
            else:
                self.puntos_jugador2 += puntos_ronda

            # Comprobar si el jugador ha alcanzado los 10,000 puntos
            if self.puntos_jugador1 >= self.max_puntuacion:
                print(f'\n🎉 ¡Jugador 1 ha ganado con {self.puntos_jugador1} puntos! 🎉')
                break
            elif self.puntos_jugador2 >= self.max_puntuacion:
                print(f'\n🎉 ¡Jugador 2 ha ganado con {self.puntos_jugador2} puntos! 🎉')
                break

            # Alternar turno
            if self.turno == 1:
                self.turno = 2
            else:
                self.turno = 1

            # Preguntar si el jugador quiere seguir
            seguir = input("¿Quieres seguir jugando? (s/n): ").lower()
            if seguir != 's':
                print(
                    f"\nGracias por jugar. Puntuaciones finales:\nJugador 1: {self.puntos_jugador1} puntos\nJugador 2: {self.puntos_jugador2} puntos")
                break



# Prueba
jugar = Farkle()
reglas = Reglas_juego()

# Muestra el menu antes de empezar el juego
jugar.mostrar_menu()
