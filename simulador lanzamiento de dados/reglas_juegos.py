

class Reglas_juego:

    def reglas_farkle(self):
        reglas = """
        --- Reglas del Farkle ---
        1️⃣ El juego se juega con 6 dados.
        2️⃣ En cada turno, lanzas los 6 dados y decides cuáles guardar para sumar puntos.
        3️⃣ Solo los números 1 y 5, tríos, escalera y combinaciones especiales suman puntos.
        4️⃣ Puedes seguir tirando los dados restantes para intentar sumar más puntos.
        5️⃣ Si en una tirada no sacas ninguna combinación válida, pierdes todos los puntos del turno (Farkle).
        6️⃣ Puedes plantarte en cualquier momento y guardar los puntos acumulados en el turno.
        7️⃣ Gana el primero en llegar a 10,000 puntos.

        --- Tabla de Puntuación ---
        🎲 Trío de 1s ➝ 300 puntos  
        🎲 Trío de cualquier otro número (2-6) ➝ Número × 100 puntos  
        🎲 1 individual ➝ 100 puntos  
        🎲 5 individual ➝ 50 puntos  
        🎲 Escalera (1,2,3,4,5,6) ➝ 1500 puntos  
        🎲 Cuatro de un mismo número ➝ Doble de los puntos del trío  
        🎲 Cinco de un mismo número ➝ Triple de los puntos del trío  
        🎲 Seis de un mismo número ➝ Cuádruple de los puntos del trío  
        """
        print(reglas)

    def reglas_mafia(self):
        reglas = '''🎲🎭 Bienvenidos al juego de dados Mafia 🎭🎲

        📜 Qué necesitas:
        - 5 dados de 6 caras por cada jugador
        - Boli y papel para anotar puntuaciones
        - Un tablero (opcional)
        
        🎲 Cómo jugar:
        1️⃣ El jugador inicial tirará los 5 dados.
        2️⃣ Si saca un **1**, ese dado se elimina del juego y pasa el turno al siguiente jugador.
        3️⃣ Si saca un **6**, deberá dar todos los 6 obtenidos al siguiente jugador, quien acumulará más dados.
        
        🏆 Quién gana:
        - El jugador que **se quede sin dados** primero.
        - O el jugador con menos dados cuando terminen las rondas acordadas.
        
        ¡Que comience el juego! 🎲🔥
        """)
        '''
        print(reglas)