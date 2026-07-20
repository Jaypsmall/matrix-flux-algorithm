import random

# CONFIGURACIÓN DEL LABORATORIO
RONDAS_MINIMAS = 8     # Base de la tesis
CAPITAL_INICIAL = 1000 # Capital inicial por partida
SIMULACIONES = 1000    # Número de partidas automáticas

class LaPekilladaCompleta:
    def __init__(self):
        self.apuestas = {"A": 1, "B": 1, "C": 1}
        self.cero = 1  # El cero empieza en 1 ficha
        self.sin_salir = {"A": 0, "B": 0, "C": 0}
        self.capital = CAPITAL_INICIAL
        self.max_apuesta = 0
        self.bancarrota = False
        self.rondas_jugadas = 0

    def ronda(self):
        if self.capital <= 0:
            self.bancarrota = True
            return

        # Control de varianza estricta: si una columna llega a 8 rondas sin salir, se fuerza su salida
        columnas_criticas = [col for col, rachas in self.sin_salir.items() if rachas >= 8]

        if columnas_criticas:
            resultado = max(columnas_criticas, key=lambda c: self.sin_salir[c])
        else:
            # Si no hay crisis, incluimos el "0" en el azar de la ruleta
            resultado = random.choice(["A", "B", "C", "0"])

        # El coste real incluye las 3 columnas + la apuesta lineal del cero
        coste = sum(self.apuestas.values()) + self.cero

        if coste > self.capital:
            self.bancarrota = True
            return

        self.capital -= coste
        self.max_apuesta = max(self.max_apuesta, max(self.apuestas.values()), self.cero)

        if resultado in ["A", "B", "C"]:
            # Gana una columna (Premio 3x)
            premio = self.apuestas[resultado] * 3
            self.capital += premio

            for col in self.apuestas:
                if col == resultado:
                    self.apuestas[col] = 1
                    self.sin_salir[col] = 0
                else:
                    self.apuestas[col] *= 2   # Duplicación geométrica de columnas perdedoras
                    self.sin_salir[col] += 1
            
            self.cero += 1  # EL CERO SUMA UNA FICHA CADA RONDA DE FORMA LINEAL
            
        else:
            # Salió el CERO (Premio 36x)
            premio = self.cero * 36
            self.capital += premio
            
            self.cero = 1  # El cero se limpia y vuelve a 1 ficha
            
            # Las columnas no han salido, así que acumulan racha y duplican
            for col in self.apuestas:
                self.apuestas[col] *= 2
                self.sin_salir[col] += 1
        
        self.rondas_jugadas += 1

    def debe_continuar(self):
        if self.rondas_jugadas < RONDAS_MINIMAS:
            return True
        
        if all(apuesta == 1 for apuesta in self.apuestas.values()) and self.cero == 1:
            return False
            
        # RETIRADA INTELIGENTE: Si ya hay ganancias netas...
        if self.capital > CAPITAL_INICIAL:
            columnas_cargadas = [ap for ap in self.apuestas.values() if ap > 1]
            # Si la exposición residual en la mesa es baja, nos retiramos con el botín
            if not columnas_cargadas or max(columnas_cargadas) < 16:
                return False 

        return True

def ejecutar_laboratorio():
    bancarrotas = 0
    supervivencias = 0
    capitales_finales = []
    max_apuesta_global = 0
    total_rondas_acumuladas = 0

    print(f"🔬 Ejecutando {SIMULACIONES} partidas (CON CERO LINEAL + VARIACIÓN HUMANA)...\n")

    for _ in range(SIMULACIONES):
        pk = LaPekilladaCompleta()
        
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

    print("=== 📊 INFORME GLOBAL COMPLETO (CON CERO) ===")
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
