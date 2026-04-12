import numpy as np
import matplotlib.pyplot as plt

def simulate_noise_to_vacuum_density():
    """
    Simulates the transition from discrete microscopic fluctuations to 
    a coarse-grained macroscopic vacuum energy density (rho_vac).
    
    This supports the claim that the 'noise' residue scales as N^(-1/2).
    """
    # 1. Setup Scaling Parameters (Matching Appendix A)
    # Total nodes in observable universe ~ 10^244
    # We simulate smaller scales and extrapolate
    n_elements = np.logspace(2, 6, 20).astype(int) 
    realizations = 100 # Monte Carlo iterations for each N
    
    mean_densities = []
    std_errors = []

    print("Starting Stochastic Noise Simulation...")
    
    for N in n_elements:
        # Simulate the BD Action fluctuation delta_S
        # According to Eq (3) and Appendix B: Var(S) proportional to N
        # Thus, delta_S follows a random distribution with std ~ sqrt(N)
        
        # Local fluctuations at each discrete element (Poisson process)
        local_fluctuations = np.random.normal(0, 1, (realizations, N))
        
        # Total action fluctuation for this realization
        delta_S = np.sum(local_fluctuations, axis=1) # Scale: sqrt(N)
        
        # Effective Density rho_vac = delta_S / Volume
        # Since Volume V is proportional to N (in Planck units)
        # rho_vac ~ sqrt(N) / N = N^(-1/2)
        rho_vac_samples = np.abs(delta_S) / N
        
        mean_densities.append(np.mean(rho_vac_samples))
        std_errors.append(np.std(rho_vac_samples))

    # 2. Extrapolation Logic
    # Fitting the simulated data to find the power-law index gamma
    coeffs = np.polyfit(np.log(n_elements), np.log(mean_densities), 1)
    gamma_fit = -coeffs[0]
    
    print(f"Empirical Scaling Exponent (Gamma): {gamma_fit:.3f}")

    # 3. Visualization for the Repository
    plt.figure(figsize=(10, 6))
    plt.errorbar(n_elements, mean_densities, yerr=std_errors, fmt='o', 
                 capsize=3, label='Monte Carlo Samples', color='blue', alpha=0.7)
    
    # Plot the theoretical prediction from Omega-TSCI
    plt.loglog(n_elements, n_elements**-0.5, 'r--', label=r'Theoretical $\mathcal{N}^{-1/2}$')
    
    plt.title("Stochastic Noise Coarse-Graining: Micro to Macro")
    plt.xlabel(r"Number of Causal Elements ($\mathcal{N}$)")
    plt.ylabel(r"Effective Noise Residue $\langle \delta \mathcal{S} \rangle / \mathcal{V}$")
    plt.legend()
    plt.grid(True, which="both", ls=":", alpha=0.5)
    
    plt.tight_layout()
    plt.savefig('noise_scaling_verification.png', dpi=300)
    print("Simulation complete. Plot saved as 'noise_scaling_verification.png'.")

if __name__ == "__main__":
    # Seed for reproducibility
    np.random.seed(42)
    simulate_noise_to_vacuum_density()
