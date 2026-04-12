import numpy as np

# Physical constants in SI units
PLANCK_LENGTH = 1.616255e-35  # meters
HUBBLE_RADIUS = 1.3e26        # meters (current observable universe)
C4_CONSTANT = 0.53            # Scaling constant from Meyer/Brightwell

def get_node_count(L):
    """
    Calculate total node count N from a given length scale L.
    Based on L = c4 * N^(1/4) * lP
    """
    return (L / (C4_CONSTANT * PLANCK_LENGTH))**4

def predict_vacuum_density(N):
    """
    Predicts the vacuum energy density ratio rho_vac / rho_Pl.
    Based on Omega-TSCI scaling: rho_ratio = N^(-1/2)
    """
    gamma = 0.50
    return N**(-gamma)
