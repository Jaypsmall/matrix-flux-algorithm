import random


# ==========================
# CONFIGURACIÓN
# ==========================

NUM_RONDAS = 1000     # Cambia aquí las rondas
APUESTA_INICIAL = 1
CAPITAL_INICIAL = 1000


# ==========================
# MOTOR PK
# ==========================

class LaPekilladaSim:

    def __init__(self):
        self.apuestas = {
            "A": APUESTA_INICIAL,
            "B": APUESTA_INICIAL,
            "C": APUESTA_INICIAL
        }

        self.capital = CAPITAL_INICIAL
        self.historial = []


    def ejecutar_ronda(self):

        # coste total de la ronda
        coste = sum(self.apuestas.values())


        # resultado aleatorio del sistema
        ganador = random.choice(
            ["A", "B", "C"]
        )


        # pago x3 de la apuesta ganadora
        premio = self.apuestas[ganador] * 3


        # balance de la ronda
        resultado = premio - coste

        self.capital += resultado


        # guardar datos
        self.historial.append({
            "ganador": ganador,
            "apuestas": self.apuestas.copy(),
            "resultado": resultado,
            "capital": self.capital
        })


        # actualizar algoritmo PK

        for columna in self.apuestas:

            if columna == ganador:
                # ganadora vuelve a 1
                self.apuestas[columna] = APUESTA_INICIAL

            else:
                # perdedoras doblan
                self.apuestas[columna] *= 2



    def simular(self, rondas):

        for i in range(rondas):
            self.ejecutar_ronda()


    def informe(self):

        print("\n===== LA PEKILLADA PK =====")

        print(
            f"Rondas ejecutadas: {len(self.historial)}"
        )

        print(
            f"Capital inicial: {CAPITAL_INICIAL}"
        )

        print(
            f"Capital final: {self.capital}"
        )

        print(
            f"Diferencia: {self.capital - CAPITAL_INICIAL}"
        )


        print("\nÚltimas 10 rondas:")

        for ronda in self.historial[-10:]:

            print(
                ronda
            )



# ==========================
# EJECUCIÓN
# ==========================

motor = LaPekilladaSim()

motor.simular(
    NUM_RONDAS
)

motor.informe()
