import matplotlib.pyplot as plt
import numpy as np

def plot_gw_spectrum():
    """
    预言随机引力波背景 (SGWB) 能谱
    Predict the SGWB spectrum
    """
    f = np.logspace(-18, -1, 100) # 频率范围 (Frequency range)
    gamma = 0.4933
    nT = 1 - 3 * gamma # 约为 -0.5
    
    # 能谱密度 (Energy density scaling)
    Omega_gw = 1e-15 * (f / 1e-16)**nT
    
    plt.loglog(f, Omega_gw, label=f'$\Omega$-TSCI Prediction ($n_T={nT:.2f}$)')
    plt.fill_between([1e-18, 1e-16], 1e-17, 1e-13, alpha=0.2, label='LiteBIRD Sensitivity Zone')
    
    plt.title("Stochastic Gravitational Wave Background")
    plt.xlabel("Frequency (Hz)"); plt.ylabel("$\Omega_{GW}(f)$")
    plt.legend(); plt.grid(True, which="both")
    plt.show()

if __name__ == "__main__":
    plot_gw_spectrum()
