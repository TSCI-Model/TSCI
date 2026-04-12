import numpy as np
import matplotlib.pyplot as plt

def generate_sgwb_comparison():
    # Frequency range for LiteBIRD (Hz)
    freq = np.logspace(-19, -14, 500)
    
    # Omega-TSCI Model: nT = -0.5 (Red Tilt)
    f_pivot = 1e-17
    omega_0 = 1e-15
    omega_tsci = omega_0 * (freq / f_pivot)**(-0.5)
    
    # Standard Inflation: nT ~ 0 (Flat)
    omega_inf = 1e-16 * np.ones_like(freq)
    
    plt.figure(figsize=(8, 6))
    plt.loglog(freq, omega_tsci, 'b-', lw=2, label=r'$\Omega$-TSCI ($n_T \approx -0.5$)')
    plt.loglog(freq, omega_inf, 'k--', label='Standard Inflation ($n_T \approx 0$)')
    
    # LiteBIRD window
    plt.axvspan(1e-18, 1e-16, color='gray', alpha=0.1, label='LiteBIRD Sensitivity')
    
    plt.xlabel('Frequency $f$ [Hz]')
    plt.ylabel(r'$\Omega_{GW}(f)$')
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.savefig('outputs/SGWB.png', dpi=300)

if __name__ == "__main__":
    generate_sgwb_comparison()
