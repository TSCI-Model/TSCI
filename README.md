# Ω-TSCI: Numerical Verification of the Causal Set Scaling Law

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Field: Theoretical Physics](https://img.shields.io/badge/Field-Theoretical%20Physics-red.svg)](https://journals.aps.org/prd/)

This repository contains the core simulation engine and visualization scripts for the **Ω-TSCI (Topological Scaling of Causal Intervals)** model. The project provides numerical evidence supporting the emergent nature of the Cosmological Constant ($\Lambda$) derived from discrete spacetime fluctuations.

## 📖 Overview

The Ω-TSCI framework demonstrates that the observable vacuum energy density is an infrared (IR) residue of Poissonian fluctuations in causal set theory. This repository reproduces the key numerical results presented in the manuscript:
* **Scaling Law Verification**: Demonstrating $\delta \mathcal{N} \sim \mathcal{N}^{1/2}$ through Monte Carlo simulations.
* **Causal Geometry**: Visualization of node distribution in 4D causal diamonds.
* **Observational Predictions**: Spectral integration of the Stochastic Gravitational Wave Background (SGWB) with $n_T \approx -0.5$.

## 🚀 Core Results

### 1. Scaling Exponent Verification
The `simulation_core.py` script performs high-precision analysis of action fluctuations.
* **Theoretical Expectation**: $\gamma = 0.5$
* **Numerical Result**: $\gamma = 0.4956 \pm 0.003$ ($R^2 > 0.999$)



### 2. SGWB Signature
Our model predicts a distinctive blue-tilted spectrum in the CMB frequency range, accessible to future missions like **LiteBIRD**.



## 🛠 Installation & Usage

### Prerequisites
- Python 3.8 or higher
- `numpy`, `scipy`, `matplotlib`

### Setup
```bash
git clone [https://github.com/TSCI-Model/TSCI.git](https://github.com/TSCI-Model/TSCI.git)
cd TSCI
pip install -r requirements.txt
