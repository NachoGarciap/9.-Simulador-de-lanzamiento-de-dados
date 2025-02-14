# 🎲 Simulador de Juegos de Dados 🎲

Un conjunto de juegos de dados hecho con Python, incluyendo Farkle, Mafia y Suma Exacta. Cada juego tiene reglas únicas y mecánicas basadas en el azar.


# 🎲 1. Farkle

Un juego de estrategia en el que los jugadores tiran 6 dados e intentan acumular puntos sin perderlos en un "Farkle".

🔹 Reglas principales:

  - Se juega con 6 dados.
  - Solo los números 1 y 5, tríos, escaleras y combinaciones especiales suman puntos.
  - Puedes seguir tirando los dados restantes para intentar sumar más puntos.
  - Si en una tirada no obtienes combinaciones válidas, pierdes todos los puntos de ese turno (Farkle).
  - Puedes plantarte en cualquier momento y guardar tus puntos acumulados.
  - El primero en llegar a 10,000 puntos gana.
    
🏆 Tabla de Puntuación:

  - Trío de 1s → 300 puntos
  - Trío de otro número (2-6) → Número × 100 puntos
  - 1 individual → 100 puntos
  - 5 individual → 50 puntos
  - Escalera (1-6) → 1500 puntos
  - Cuatro iguales → Doble de los puntos del trío
  - Cinco iguales → Triple de los puntos del trío
  - Seis iguales → Cuádruple de los puntos del trío
    
# 🎲 2. Mafia
Un juego en el que los jugadores intentan quedarse sin dados lo más rápido posible.

🔹 Reglas principales:

  - Cada jugador tira 5 dados.
  - Si un jugador saca un 1, ese dado se elimina del juego.
  - Si un jugador saca un 6, debe dar todos los 6 obtenidos al siguiente jugador.
  - El jugador que se quede sin dados primero o que tenga menos dados al final de las rondas gana.
    
# 🎲 3. Suma Exacta
Un juego de precisión donde los jugadores deben alcanzar exactamente 15 puntos con tres dados.

🔹 Reglas principales:

  - Cada jugador lanza 3 dados de 6 caras por turno.
  - Si la suma es exactamente 15, el jugador gana inmediatamente.
  - Si la suma es mayor de 15, el jugador pierde su turno.
  - Si la suma es menor de 15, el jugador suma esos puntos a su total.
  - El primero en alcanzar 30 puntos o más gana.
