import numpy as np

# Constants
gamma = 0.4933
c = 299792458.0
G = 6.67430e-11
M_sun = 1.98847e30
AU = 1.4959787e11
mu_E = 3.986004418e14 # Earth's standard gravitational parameter

# Solar gravity at 1 AU
gS = G * M_sun / (AU**2)

# Satellites from the user's image data
sats = {
    "C11 (MEO)": 27905729.0,
    "C14 (MEO)": 27905729.0, # MEO satellites have almost identical a
    "C10 (IGSO)": 42161229.0
}

results = {}
for name, a in sats.items():
    # Calculate angular velocity
    omega = np.sqrt(mu_E / a**3)
    # Calculate theoretical amplitude: A = (gamma * gS * a) / (omega * c^2)
    A = (gamma * gS * a) / (omega * c**2)
    p2p = 2 * A * 1e9 # Peak to peak in ns
    
    # Calculate decoherence rate for 10g mass at 1 micrometer
    m_macro = 0.01 # 10g
    dx = 1e-6 # 1 um
    hbar = 1.0545718e-34
    tP = 5.391247e-44
    rate = (m_macro**2 * gamma**2 * tP * (gS * dx)**2) / (2 * hbar**2)
    
    results[name] = {
        "a (km)": a / 1000,
        "omega (rad/s)": omega,
        "Period (hours)": 2 * np.pi / omega / 3600,
        "Amplitude (ns)": A * 1e9,
        "Peak-to-Peak (ns)": p2p,
        "Max Decoherence (s^-1)": rate
    }

print(results)
