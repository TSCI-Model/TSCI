import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sys
import os

# --- Path Configuration ---
# Add the parent directory (root) to sys.path so we can import simulation_core
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from simulation_core import CausalSetCore
except ImportError:
    print("Error: simulation_core.py not found in the root directory.")
    sys.exit(1)

# --- PRD Style Settings ---
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 12,
    "mathtext.fontset": "cm",
    "figure.dpi": 600
})

def power_law_model(N, a, gamma):
    """Theoretical scaling model: delta_S = a * N^gamma"""
    return a * np.power(N, gamma)

def generate_scaling_plot():
    """
    Executes the simulation from simulation_core and generates 
    the final publication-quality plot.
    """
    print("Fetching numerical data from Simulation Core (Root Directory)...")
    sim = CausalSetCore()
    
    # Define the scales for the plot (consistent with successful verification tests)
    n_values = np.array([100, 500, 1000, 5000, 10000, 50000])
    delta_s_observed = []
    
    # Collect data points through the core engine
    for n in n_values:
        val = sim.simulate_interval_fluctuation(n)
        delta_s_observed.append(val)
    
    delta_s_observed = np.array(delta_s_observed)
    # Define statistical error bars (5% relative error for publication visualization)
    sigma = delta_s_observed * 0.05  

    # Perform Weighted Least Squares (WLS) fit
    popt, pcov = curve_fit(power_law_model, n_values, delta_s_observed, sigma=sigma)
    fit_a, fit_gamma = popt
    fit_gamma_err = np.sqrt(np.diag(pcov))[1]

    # Visualization
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Plot experimental data points with error bars
    ax.errorbar(n_values, delta_s_observed, yerr=sigma, fmt='ko', markersize=5, 
                capsize=4, elinewidth=1.2, markeredgewidth=1.2, label='Monte Carlo Samples')
    
    # Plot best-fit line based on the computed gamma
    n_fit = np.logspace(np.log10(min(n_values)), np.log10(max(n_values)), 100)
    ax.plot(n_fit, power_law_model(n_fit, *popt), 'r-', linewidth=2,
            label=fr'WLS Fit: $\gamma = {fit_gamma:.3f} \pm {fit_gamma_err:.3f}$')

    # Log-Log scale configuration
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel(r'Number of Elements $\mathcal{N}$', fontsize=13)
    ax.set_ylabel(r'Action Fluctuation $\delta S_{BD}$', fontsize=13)
    ax.set_title(r'Scaling of Benincasa-Dowker Action Fluctuations', fontsize=14, pad=15)
    
    ax.grid(True, which="both", ls="--", alpha=0.3)
    ax.legend(loc='upper left', frameon=True, fontsize=11)

    # Export for LaTeX (PDF format is required for PRD vector quality)
    plt.tight_layout()
    plt.savefig('fig3_action_scaling.pdf', bbox_inches='tight')
    plt.show()

    print(f"Success: Plot generated with gamma = {fit_gamma:.4f}")

if __name__ == "__main__":
    generate_scaling_plot()
