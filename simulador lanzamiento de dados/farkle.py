import random


class Farkle:

    def __init__(self):
        print('--- Farkle ---')
        self.dado = [1, 2, 3, 4, 5, 6]

    def lanzar_dado(self, cantidad=6):
        resultados = []
        for _ in range(cantidad):
            resultado = random.choice(self.dado)
            resultados.append(resultado)
        print(f"Resultado de {cantidad} dados: {resultados}")
        return resultados

    def calcular_puntos(self):
        dados_lanzados = self.lanzar_dado()
        puntos = 0
        contador = {}
        for dado in dados_lanzados:
            if dado in contador:
                contador[dado] += 1
            else:
                contador[dado] = 1

        print(f'Contador de números: {contador}')

        for valor, cantidad in contador.items():
            # Puntos 3 dados iguales
            if cantidad >= 3:
                if valor == 1:
                    puntos += 1000  # tres unos
                else:
                    puntos += valor * 100  # Tres de cualquier otro número

            # Dados extra 1=100puntos 5=50puntos
            if valor == 1:
                puntos += cantidad * 100  # Cada 1 suma 100 puntos
            elif valor == 5:
                puntos += cantidad * 50  # Cada 5 suma 50 puntos

        # escalera de 1 al 6
        if set(dados_lanzados) == {1, 2, 3, 4, 5, 6}:
            puntos += 1500  # escalera completa
            print("¡Escalera completa! 1500 puntos.")
        else:
            print('No hay escalera!')

        print(f'Total puntos: {puntos}')


# Prueba
prueba = Farkle()
prueba.calcular_puntos()
