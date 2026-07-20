import sys
import random

class SimuladorTesisMatemática:
    def __init__(self, fichas_propias, fichas_banca):
        self.u = 1  # Unidad base: 1 ficha
        self.columnas = {'A': self.u, 'B': self.u, 'C': self.u}
        self.sequia = {'A': 0, 'B': 0, 'C': 0}
        
        self.capital_propio = fichas_propias
        self.capital_banca = fichas_banca
        self.ronda = 1

    def ejecutar_simulacion(self):
        print(f"[*] Iniciando tesis con {self.capital_propio} U frente a {self.capital_banca} U de la banca.")
        
        # El algoritmo corre de forma abstracta mientras ambos tengan fichas
        while self.capital_propio > 0 and self.capital_banca > 0:
            # Sumamos el coste total de las tres columnas en esta ronda
            coste_ronda = sum(self.columnas.values())
            
            # Control de quiebra: si el muelle pide más de lo que nos queda, se rompe la secuencia
            if coste_ronda > self.capital_propio:
                print(f"\n[!] Simulación terminada en ronda {self.ronda}: Ruina por falta de liquidez.")
                print(f" -> El muelle exigía {coste_ronda} fichas, pero solo quedaban {self.capital_propio}.")
                break
                
            self.capital_propio -= coste_ronda
            
            # Simulamos el comportamiento aleatorio del tablero (Columnas A, B o C)
            resultado = random.choice(['A', 'B', 'C'])
            
            # Pago de la columna ganadora (Retorno 3:1)
            premio = self.columnas[resultado] * 3
            self.capital_propio += premio
            
            # Balance contra la banca simulada
            balance = premio - coste_ronda
            self.capital_banca -= balance
            
            # Actualizamos las dinámicas de duplicación geométrica
            for col in self.columnas:
                if col == resultado:
                    self.columnas[col] = self.u  # Perfil bajo al ganar
                else:
                    self.columnas[col] *= 2      # Duplicación elástica
            
            self.ronda += 1
            
        if self.capital_banca <= 0:
            print(f"\n[+] Tesis validada en ronda {self.ronda}: La banca simulada se ha quedado sin fichas.")

if __name__ == "__main__":
    # Permite ejecutar el script pasando tus fichas como argumento en la terminal
    fichas_usuario = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    fichas_casino = int(sys.argv[2]) if len(sys.argv) > 2 else 500
    
    simulador = SimuladorTesisMatemática(fichas_usuario, fichas_casino)
    simulador.ejecutar_simulacion()

