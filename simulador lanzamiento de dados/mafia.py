import random

from reglas_juegos import Reglas_juego


class Mafia:
    def __init__(self, jugadores=2, dados_por_jugador=5):
        self.jugadores = jugadores
        self.dados = [dados_por_jugador] * jugadores  # Lista con la cantidad de dados de cada jugador
        self.dados_por_jugador = dados_por_jugador  # Almacena los dados por jugador
        self.dado = [1, 2, 3, 4, 5, 6]  # Caras del dado
        self.turno = 0  # Jugador actual (índice de la lista)
        self.reglas = Reglas_juego()

    def lanzar_dados(self):
        cantidad = self.dados[self.turno]  # Dados actuales del jugador
        resultados = []
        for _ in range(cantidad):
            resultado = random.choice(self.dado)
            resultados.append(resultado)

        print(f"\n🎲 Jugador {self.turno + 1} lanza {cantidad} dados: {', '.join(map(str, resultados))}")
        return resultados

    def aplicar_reglas(self, resultados):
        uno = resultados.count(1)  # Contar cuántos unos hay
        seis = resultados.count(6)  # Contar cuántos seises hay

        # Restar los dados eliminados
        self.dados[self.turno] -= uno

        # Pasar los seises al siguiente jugador
        siguiente = (self.turno + 1) % self.jugadores
        self.dados[siguiente] += seis

        print(f"📉 Jugador {self.turno + 1} pierde {uno} dados.")
        print(f"🎁 Jugador {siguiente + 1} recibe {seis} dados extra.")

    def jugar_ronda(self):
        resultados = self.lanzar_dados()
        self.aplicar_reglas(resultados)
        self.turno = (self.turno + 1) % self.jugadores  # Cambiar turno

    def jugar(self):
        while all(d > 0 for d in self.dados):  # Mientras todos tengan al menos 1 dado
            print(f"\n📢 Estado de los jugadores: {self.dados}")
            self.jugar_ronda()

        print(f"\n🏆 ¡Fin del juego! Ganador: Jugador {self.dados.index(min(self.dados)) + 1}")

    def mostrar_menu(self):
        while True:
            print('🎲----- Bienvenidos al juego Mafia -----🎲')
            print('1. Reglas')
            print('2. Jugar')
            print('3. Salir')

            try:
                opcion = int(input("Elige un modo de juego: "))
            except ValueError:
                print('Introduce una opcion valida, por favor.')
                continue  # asi vuelve a iniciar el try hasta que la opcion sea correcta

            if opcion == 1:
                print('----- Recordatorio de las reglas y los puntos! -----')
                self.reglas.reglas_mafia()
            elif opcion == 2:
                print('----- Empieza la partida! -----')
                # Imprime el número de jugadores
                print(f"🎲 Número de jugadores: {self.jugadores}")
                print(f"🎲 Dados por jugador: {self.dados_por_jugador}")
                print(f"🎲 Dados de cada jugador: {self.dados}")
                self.jugar()
            elif opcion == 3:
                print('Saliendo del juego...')
                break
            else:
                print('Introduce una opcion valida')
