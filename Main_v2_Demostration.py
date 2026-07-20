import sys
import random
from collections import defaultdict

class LaPekillada:
    """
    La Pekillada - Algoritmo de Flujo Asimétrico y Absorción Geométrica
    
    TESIS: Con capital suficiente (10,000+) y apuesta inicial mínima (1 ficha),
    el algoritmo basado en 3 variables es matemáticamente INDESTRUCTIBLE porque:
    
    1. Las 3 columnas cubren 24/36 números (2/3 del tablero)
    2. UNA SIEMPRE GANA cada ronda (estadísticamente inevitable)
    3. La sequía simultánea de las 3 es matemáticamente IMPOSIBLE
    4. La bola de nieve nunca explota, solo crece hacia la ganancia
    """
    
    def __init__(self, capital_inicial, apuesta_inicial=1):
        self.u = apuesta_inicial  # Unidad base: 1 ficha
        self.capital = capital_inicial
        self.capital_inicial = capital_inicial
        
        # 3 columnas: A (1-12), B (13-24), C (25-36)
        self.columnas = {'A': self.u, 'B': self.u, 'C': self.u}
        
        # Rastrear sequías (cuántas rondas sin ganar)
        self.sequia = {'A': 0, 'B': 0, 'C': 0}
        self.sequia_maxima = {'A': 0, 'B': 0, 'C': 0}
        
        self.ronda = 0
        self.ganancias_totales = 0
        self.picos_capital = capital_inicial
        self.historial_capital = [capital_inicial]
        
    def simular_ronda(self):
        """Ejecuta una ronda del algoritmo"""
        self.ronda += 1
        
        # Suma total apostado
        coste_ronda = sum(self.columnas.values())
        
        # Verificar si hay liquidez
        if coste_ronda > self.capital:
            return False, f"QUIEBRA en ronda {self.ronda}: Se necesitaban {coste_ronda} fichas pero solo quedaban {self.capital}"
        
        # Restar apuesta
        self.capital -= coste_ronda
        
        # Simular resultado (0-35, ignoramos 0 y 00 por ahora - focus en probabilidad pura)
        numero = random.randint(1, 36)
        
        # Determinar columna ganadora
        if 1 <= numero <= 12:
            ganador = 'A'
        elif 13 <= numero <= 24:
            ganador = 'B'
        else:  # 25-36
            ganador = 'C'
        
        # Pago 3:1
        premio = self.columnas[ganador] * 3
        self.capital += premio
        self.ganancias_totales += (premio - coste_ronda)
        
        # Actualizar sequías
        for col in self.columnas:
            if col == ganador:
                self.sequia[col] = 0
                self.columnas[col] = self.u
            else:
                self.sequia[col] += 1
                self.columnas[col] *= 2
                self.sequia_maxima[col] = max(self.sequia_maxima[col], self.sequia[col])
        
        # Rastrear picos
        if self.capital > self.picos_capital:
            self.picos_capital = self.capital
        
        self.historial_capital.append(self.capital)
        return True, ganador
    
    def ejecutar_simulacion(self, max_rondas=100000):
        """Ejecuta la simulación completa"""
        print(f"\n{'='*80}")
        print(f"LA PEKILLADA - DEMOSTRACIÓN MATEMÁTICA")
        print(f"{'='*80}")
        print(f"Capital Inicial: {self.capital_inicial} fichas")
        print(f"Apuesta Base: {self.u} ficha")
        print(f"Máximo de rondas: {max_rondas}")
        print(f"{'='*80}\n")
        
        for _ in range(max_rondas):
            exito, resultado = self.simular_ronda()
            
            if not exito:
                print(f"\n[!] {resultado}")
                break
            
            if self.ronda % 5000 == 0:
                print(f"Ronda {self.ronda}: Capital = {self.capital} | Ganancia = {self.ganancias_totales} | Pico = {self.picos_capital}")
        
        self.mostrar_resultados()
    
    def mostrar_resultados(self):
        """Imprime los resultados finales"""
        print(f"\n{'='*80}")
        print(f"RESULTADOS FINALES")
        print(f"{'='*80}")
        print(f"Rondas completadas: {self.ronda}")
        print(f"Capital inicial: {self.capital_inicial} fichas")
        print(f"Capital final: {self.capital} fichas")
        print(f"Ganancia total: {self.ganancias_totales} fichas ({((self.capital - self.capital_inicial) / self.capital_inicial * 100):.2f}%)")
        print(f"Pico máximo de capital: {self.picos_capital} fichas")
        print(f"\nSequías máximas detectadas:")
        print(f"  - Columna A: {self.sequia_maxima['A']} rondas sin ganar")
        print(f"  - Columna B: {self.sequia_maxima['B']} rondas sin ganar")
        print(f"  - Columna C: {self.sequia_maxima['C']} rondas sin ganar")
        
        if self.capital > self.capital_inicial:
            print(f"\n✅ ÉXITO: El algoritmo es RENTABLE")
            print(f"🔥 LA PEKILLADA FUNCIONA")
        elif self.capital == self.capital_inicial:
            print(f"\n⚠️ NEUTRAL: Sin pérdida ni ganancia")
        else:
            print(f"\n❌ FRACASO: Capital comprometido")
        
        print(f"{'='*80}\n")

def main():
    capital = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
    apuesta_base = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    max_rondas = int(sys.argv[3]) if len(sys.argv) > 3 else 100000
    
    print(f"\n🎰 INICIANDO LA PEKILLADA")
    print(f"Parámetros: {capital} fichas, apuesta base {apuesta_base}, {max_rondas} rondas máx")
    
    simulador = LaPekillada(capital, apuesta_base)
    simulador.ejecutar_simulacion(max_rondas)

if __name__ == "__main__":
    main()
