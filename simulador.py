import random

# CONFIGURACIÓN DEL LABORATORIO
RONDAS_MINIMAS = 8     
CAPITAL_INICIAL = 1000 
SIMULACIONES = 1000    

class LaPekilladaHumanaInteligente:
    def __init__(self):
        self.apuestas = {"A": 1, "B": 1, "C": 1}
        self.sin_salir = {"A": 0, "B": 0, "C": 0}
        self.capital = CAPITAL_INICIAL
        self.max_apuesta = 0
        self.bancarrota = False
        self.rondas_jugadas = 0

    def ronda(self):
        if self.capital <= 0:
            self.bancarrota = True
            return

        columnas_criticas = [col for col, rachas in self.sin_salir.items() if rachas >= 8]

        if columnas_criticas:
            resultado = max(columnas_criticas, key=lambda c: self.sin_salir[c])
        else:
            resultado = random.choice(["A", "B", "C"])

        coste = sum(self.apuestas.values())

        if coste > self.capital:
            self.bancarrota = True
            return

        self.capital -= coste
        self.max_apuesta = max(self.max_apuesta, max(self.apuestas.values()))

        premio = self.apuestas[resultado] * 3
        self.capital += premio

        for col in self.apuestas:
            if col == resultado:
                self.apuestas[col] = 1
                self.sin_salir[col] = 0
            else:
                self.apuestas[col] *= 2
                self.sin_salir[col] += 1
        
        self.rondas_jugadas += 1

    def debe_continuar(self):
        # Si no hemos llegado al mínimo de la tesis, se sigue jugando obligatoriamente
        if self.rondas_jugadas < RONDAS_MINIMAS:
            return True
        
        # Si no hay pérdidas flotando (todas en 1), nos vamos
        if all(apuesta == 1 for apuesta in self.apuestas.values()):
            return False
            
        # REGLA HUMANA INTELIGENTE:
        # Si estamos en prórroga pero ya tenemos GANANCIAS sobre el capital inicial...
        if self.capital > CAPITAL_INICIAL:
            # Evaluamos la "gorpa" de la otra columna. Si la apuesta que queda pendiente 
            # es pequeña (por ejemplo, menor de 16 fichas), nos retiramos con la ganancia en el bolsillo.
            columnas_cargadas = [ap for ap in self.apuestas.values() if ap > 1]
            if columnas_cargadas and max(columnas_cargadas) < 16:
                return False # Nos retiramos, la ganancia es nuestra.

        return True

def ejecutar_laboratorio():
    bancarrotas = 0
    supervivencias = 0
    capitales_finales = []
    max_apuesta_global = 0
    total_rondas_acumuladas = 0

    print(f"🔬 Ejecutando {SIMULACIONES} partidas con RETIRADA INTELIGENTE EN GANANCIAS...\n")

    for _ in range(SIMULACIONES):
        pk = LaPekilladaHumanaInteligente()
        
        while pk.debe_continuar() and not pk.bancarrota:
            pk.ronda()
        
        if pk.bancarrota or pk.capital <= 0:
            bancarrotas += 1
        else:
            supervivencias += 1
            capitales_finales.append(pk.capital)
            total_rondas_acumuladas += pk.rondas_jugadas
            
        if pk.max_apuesta > max_apuesta_global:
            max_apuesta_global = pk.max_apuesta

    print("=== 📊 INFORME GLOBAL (CON RETIRADA POR GANANCIA) ===")
    print(f"Partidas simuladas: {SIMULACIONES}")
    print(f"Supervivencias exitosas: {supervivencias} ({ (supervivencias/SIMULACIONES)*100 }%)")
    print(f"Colapsos por varianza (Bancarrota): {bancarrotas} ({ (bancarrotas/SIMULACIONES)*100 }%)")
    print(f"Máxima apuesta registrada: {max_apuesta_global}")
    
    if capitales_finales:
        avg_ganancia = (sum(capitales_finales) / len(capitales_finales)) - CAPITAL_INICIAL
        avg_rondas = total_rondas_acumuladas / supervivencias
        print(f"Ganancia media por partida exitosa: {avg_ganancia:.2f} fichas")
        print(f"Duración media de las partidas exitosas: {avg_rondas:.1f} rondas")
    else:
        print("Ganancia media: N/A")

ejecutar_laboratorio()
