import random


class LanzarDado:

    def __init__(self):
        # Diferentes dados
        self.dados = {
            'd6': [1, 2, 3, 4, 5, 6],
            'd8': [1, 2, 3, 4, 5, 6, 7, 8],
            'd10': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'd12': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            'd20': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        }

    def lanzar_dado(self, tipo_dado):

        # Verificar si el tipo de dado ingresado es válido
        if tipo_dado in self.dados:
            resultado = random.choice(self.dados[tipo_dado])
            print('-------------------------------------')
            print(f"Resultado del dado {tipo_dado}: {resultado}")
            print('-------------------------------------')
        else:
            print(f"El dado {tipo_dado} no está disponible.")

    def mostrar_menu(self):
        while True:
            print('-*-*- Elige un dado: -*-*-')
            print('| 1. Dado de 6 caras:  |')
            print('| 2. Dado de 8 caras:  |')
            print('| 3. Dado de 10 caras: |')
            print('| 4. Dado de 12 caras: |')
            print('| 5. Dado de 20 caras: |')
            print('| 6. Salir             |')
            print('------------------------')

            try:
                opcion = int(input('Elige una opción por favor: '))
            except ValueError:
                print('Por favor, ingresa un número válido.')
                continue

            if opcion == 1:
                self.lanzar_dado('d6')
            elif opcion == 2:
                self.lanzar_dado('d8')
            elif opcion == 3:
                self.lanzar_dado('d10')
            elif opcion == 4:
                self.lanzar_dado('d12')
            elif opcion == 5:
                self.lanzar_dado('d20')
            elif opcion == 6:
                print('Saliendo del programa...')
                break
            else:
                print('Introduce una opcion valida')


