import numpy as np
import matplotlib.pyplot as plt

def generate_causal_diamond_v2(N=600):
    """
    Generate and plot a 2D Causal Diamond projection.
    Updated for PRD publication standards with corrected LaTeX rendering.
    """
    # Generate Poissonian sprinkling in light-cone coordinates (u, v)
    u = np.random.uniform(0, 1, N)
    v = np.random.uniform(0, 1, N)
    
    # Transform to spacetime coordinates (t, x)
    t = (u + v) / 2
    x = (v - u) / 2
    
    # Define causal boundaries (Diamond shape)
    boundary_x = [0, 0.5, 0, -0.5, 0]
    boundary_t = [0, 0.5, 1, 0.5, 0]
    
    # Set plot style to match PRD font and high resolution
    plt.rcParams.update({
        "font.family": "serif",
        "mathtext.fontset": "cm",
        "font.size": 11
    })
    
    plt.figure(figsize=(8, 8), dpi=600)
    
    # Plotting: Using raw strings r'' to ensure proper LaTeX rendering of \mathcal
    plt.scatter(x, t, s=12, c='black', alpha=0.7, edgecolors='none', 
                label=r'Sprinkled Nodes ($\mathcal{N}=' + str(N) + r'$)')
    
    # Draw the Causal Horizon/Boundary
    plt.plot(boundary_x, boundary_t, color='#d62728', lw=2.5, label='Causal Horizon')
    plt.fill(boundary_x, boundary_t, color='#1f77b4', alpha=0.08)
    
    # Formatting axes and labels
    plt.xlabel(r'Spatial Coordinate $x$', fontsize=12)
    plt.ylabel(r'Time Coordinate $t$', fontsize=12)
    plt.title(r'$\Omega$-TSCI Model: Causal Diamond Projection', fontsize=14)
    
    plt.legend(loc='upper right', frameon=True, fontsize=10)
    plt.grid(True, linestyle=':', alpha=0.5)
    plt.gca().set_aspect('equal', adjustable='box')
    
    # Exporting high-resolution vector PDF for publication
    plt.tight_layout()
    plt.savefig('fig2_causal_diamond.pdf', bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    generate_causal_diamond_v2()
