import numpy as np
import matplotlib.pyplot as plt

def generate_sgwb_spectrum_english():
    """
    Generate the Stochastic Gravitational Wave Background (SGWB) power spectrum.
    Formatted for Physical Review D (PRD) publication standards.
    """
    # Set PRD publication style parameters
    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 12,
        "mathtext.fontset": "cm",
        "figure.dpi": 600
    })

    # Frequency range: From Hubble scale to CMB scale (Hz)
    freq = np.logspace(-19, -15, 100)
    
    # 1. Ω-TSCI Model Prediction: n_T ≈ -0.5
    f_H = 2.3e-18  # Current Hubble frequency
    A_tsci = 1e-15 # Predicted amplitude baseline 
    n_T = -0.5
    omega_gw = A_tsci * (freq / f_H)**n_T

    # 2. Baseline: Standard Inflationary Model (n_T ≈ 0)
    omega_inflation = 1e-16 * np.ones_like(freq)

    # 3. Detector Sensitivity (Estimated LiteBIRD threshold)
    litebird_sens = 5e-16 * (freq / 1e-17)**0.2 

    plt.figure(figsize=(9, 6))
    
    # Plotting theoretical models
    plt.loglog(freq, omega_gw, 'r-', linewidth=2, 
               label=r'$\Omega$-TSCI Prediction ($n_T \approx -0.5$)')
    plt.loglog(freq, omega_inflation, 'k--', alpha=0.6, 
               label=r'Standard Inflation ($n_T \approx 0$)')
    
    # Shaded region for detector sensitivity
    plt.fill_between(freq, 1e-20, litebird_sens, color='blue', alpha=0.1, 
                    label='LiteBIRD Sensitivity Reach')

    # Mark critical physical scale (Hubble Frequency)
    plt.axvline(x=f_H, color='gray', linestyle=':', label=r'Hubble Frequency $f_H$')

    # Axis labeling and formatting
    plt.xlabel('Frequency $f$ [Hz]', fontsize=12)
    plt.ylabel(r'Energy Density $\Omega_{gw}(f)$', fontsize=12)
    plt.title('Predicted SGWB Power Spectrum: $\Omega$-TSCI vs. Inflation', fontsize=14)
    
    plt.ylim(1e-17, 1e-13)
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.legend(loc='upper right', fontsize=10)
    
    # Export as high-resolution PDF (preferred for PRD)
    plt.tight_layout()
    plt.savefig('fig4_sgwb_spectrum.pdf', bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    generate_sgwb_spectrum_english()