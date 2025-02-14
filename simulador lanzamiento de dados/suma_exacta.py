import random

from reglas_juegos import Reglas_juego


class SumaExacta:

    def __init__(self):
        self.d6 = [1, 2, 3, 4, 5, 6]  # Caras del dado
        self.turno = 0  # Jugador actual (0 = Jugador 1, 1 = Jugador 2)
        self.puntajes = [0, 0]  # Puntos de los jugadores
        self.reglas = Reglas_juego()

    def lanzar_dado(self, cantidad=3):
        resultados = []

        for _ in range(cantidad):
            resultado = random.choice(self.d6)
            resultados.append(resultado)

        print(f"🎲 Jugador {self.turno + 1} lanza: {resultados}")
        return sum(resultados)

    def comprobar_puntos(self):
        puntos = self.lanzar_dado()

        if puntos == 15:
            print(f"Jugador {self.turno + 1} ha ganado con una tirada exacta de 15!")
            return True  # Termina el juego
        elif puntos > 15:
            print("❌ Te pasaste de 15. Pierdes el turno.")
        else:
            self.puntajes[self.turno] += puntos
            print(f"Puntuación actual: Jugador 1 - {self.puntajes[0]} | Jugador 2 - {self.puntajes[1]}")

            if self.puntajes[self.turno] >= 30:
                print(f"🏆 ¡Jugador {self.turno + 1} ha ganado con {self.puntajes[self.turno]} puntos!")
                return True  # Termina el juego

        return False  # Si no ha ganado nadie, el juego sigue

    def jugar(self):
        while True:
            print(f"\n----- Turno de Jugador {self.turno + 1} -----")
            if self.comprobar_puntos():
                break  # Si hay un ganador, salir del bucle

            # Cambiar turno
            self.turno = 1 - self.turno

    def mostrar_menu(self):
        while True:
            print("🎲 Bienvenidos a Suma Exacta 🎲")
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
                self.reglas.reglas_suma_exacta()
            elif opcion == 2:
                print('----- Empieza la partida! -----')
                self.jugar()
            elif opcion == 3:
                print('Saliendo del juego...')
                break
            else:
                print('Introduce una opcion valida')


