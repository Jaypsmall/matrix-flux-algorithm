# 🔬 La Pekillada
## Asymmetric Flow & Geometric Absorption Algorithm

---

![Status](https://img.shields.io/badge/status-experimental-orange)
![Language](https://img.shields.io/badge/python-simulation-blue)
![Category](https://img.shields.io/badge/category-mathematical%20model-purple)

---

# 📌 Overview

**La Pekillada** is a theoretical computational model focused on the study of dynamic capital distribution across three simultaneous variables.

The project explores an asymmetric flow system where each variable maintains an independent exposure state and adapts according to previous events.

Created and documented by:

**@Jaypsmall**

Project name:

**"La Pekillada"**

---

# 🧠 Concept

The algorithm is based on an elastic distribution system:

- Three independent variables operate simultaneously.
- The successful variable returns to minimum exposure.
- The unsuccessful variables increase their exposure progressively.
- The system studies whether accumulated exposure can be absorbed by future positive events.

The objective is to analyze the behavior of progressive allocation systems under different statistical conditions.

---

# ⚙️ Algorithm Logic

The model follows these rules:

## Initial State

```text
A = 1
B = 1
C = 1
```

Each variable starts with the minimum exposure unit.

---

## Event Resolution

When an event occurs:

### Winning Variable

The winning variable returns to the minimum value:

```text
Winner = 1
```

---

### Losing Variables

The losing variables increase:

```text
Loser = Loser × 2
```

Example:

```text
Initial:

A = 1
B = 1
C = 1


Event:

A wins


New state:

A = 1
B = 2
C = 2
```

---

# 📊 Mathematical Model

The system studies:

- Exposure accumulation
- Capital consumption
- Geometric progression
- Variance impact
- Recovery behaviour
- Maximum risk thresholds

Main variables:

```text
R = Available resources

E = Exposure level

V = Variance

T = Number of iterations
```

---

# 🔬 Simulation Environment

The repository works as a mathematical laboratory.

Possible experiments:

- 100 rounds
- 1,000 rounds
- 100,000 rounds
- Monte Carlo simulations

Metrics evaluated:

✅ Final balance  
✅ Maximum exposure reached  
✅ Maximum drawdown  
✅ Recovery periods  
✅ System stability  

---

# 🛡️ Risk Analysis

This project does not claim guaranteed profitability.

The model studies the point where:

- Geometric growth exceeds available capital.
- External limits affect execution.
- Variance creates extreme scenarios.

Important factors:

- Starting capital
- Maximum allowed exposure
- Number of iterations
- External constraints

---

# 🧪 Experimental Validation

Validation is performed through:

## Monte Carlo Analysis

Thousands of independent simulations can be executed to measure:

- Probability distribution
- Average results
- Extreme events
- Risk of exhaustion

---

# 📂 Project Structure

```text
matrix-flux-algorithm/

│
├── main.py
├── simulator.py
├── README.md
├── results/
│   └── simulations.csv
│
└── docs/
    └── thesis.md
```

---

# 🚀 Usage

Clone repository:

```bash
git clone https://github.com/Jaypsmall/matrix-flux-algorithm
```

Run simulation:

```bash
python main.py
```

Configure parameters:

```python
ROUNDS = 1000
INITIAL_CAPITAL = 10000
INITIAL_UNIT = 1
```

---

# 🔮 Future Development

Possible improvements:

- Real-time visualization
- Statistical dashboard
- Monte Carlo engine
- Risk heatmaps
- Probability analysis
- Machine learning pattern detection

---

# 📚 Documentation

Full theoretical description:

[Read the complete thesis](docs/THESIS.md)

---

# 📜 Project Information

**Name:**

La Pekillada

**Technical Name:**

Asymmetric Flow & Geometric Absorption Algorithm

**Creator:**

@Jaypsmall

**Type:**

Experimental mathematical simulation model

**Status:**

Research and development phase

---

# ⚠️ Disclaimer

This repository is an experimental mathematical model created for simulation and educational purposes.

It is intended to study dynamic allocation systems and statistical behaviour.

It should not be interpreted as a guarantee of financial performance or prediction capability.

---

# ✍️ Attribution

If referencing this model, please cite:

> "La Pekillada - Asymmetric Flow & Geometric Absorption Algorithm, created and documented by @Jaypsmall."

---

© 2026 @Jaypsmall
