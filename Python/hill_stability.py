import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Circle

# Constants
G = 6.67430e-11
M_star = 1.989e30  # Solar mass
m1, m2 = 5.972e24, 1.898e27  # Earth, Jupiter masses

# Orbital parameters - m1 now has elliptical orbit
a1, e1 = 1.496e11, 0.0167  # Earth's semi-major axis and eccentricity
a2 = 7.783e11  # Jupiter's semi-major axis (circular)

# Calculate periods with adjusted speeds
T1 = 2 * np.pi * np.sqrt(a1**3 / (G * M_star)) * 0.6  # 60% of real period
T2 = 2 * np.pi * np.sqrt(a2**3 / (G * M_star)) * 0.9  # 30% of real period

# Time array - enough for 2 full rotations
t = np.linspace(0, 2*max(T1, T2), 500)  # More frames for smooth ellipse

# True anomaly calculation for elliptical orbit (m1)
def true_anomaly(t, T, e):
    M = 2 * np.pi * t / T  # Mean anomaly
    # Approximate solution to Kepler's equation
    E = M + e * np.sin(M)  # Eccentric anomaly (first order approximation)
    nu = 2 * np.arctan(np.sqrt((1+e)/(1-e)) * np.tan(E/2))  # True anomaly
    return nu

theta1 = true_anomaly(t, T1, e1)
theta2 = 2 * np.pi * t / T2  # Circular orbit for m2

# Elliptical orbit coordinates for m1
r1 = a1 * (1 - e1**2) / (1 + e1 * np.cos(theta1))
x1, y1 = r1 * np.cos(theta1), r1 * np.sin(theta1)

# Circular orbit for m2
x2, y2 = a2 * np.cos(theta2), a2 * np.sin(theta2)

# Plot setup
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1.2*a2, 1.2*a2)
ax.set_ylim(-1.2*a2, 1.2*a2)
ax.set_aspect("equal")
ax.axis('off')

# Central star - offset to focus for elliptical orbit
star = Circle((a1*e1, 0), 0.08*a1, color="gold", zorder=10)  # Star at focus
ax.add_patch(star)

# Orbiting bodies
m1_dot, = ax.plot([], [], 'bo', markersize=6, zorder=5)
m2_dot, = ax.plot([], [], 'ro', markersize=7, zorder=5)

# Discontinuous orbit trails (properly spaced for ellipse)
m1_trail, = ax.plot([], [], 'b--', alpha=0.7, linewidth=1, dashes=(5, 3))
m2_trail, = ax.plot([], [], 'r--', alpha=0.7, linewidth=1, dashes=(5, 3))

# Initialize
def init():
    m1_dot.set_data([], [])
    m2_dot.set_data([], [])
    m1_trail.set_data([], [])
    m2_trail.set_data([], [])
    return m1_dot, m2_dot, m1_trail, m2_trail

# Update function with proper elliptical sampling
def update(frame):
    m1_dot.set_data([x1[frame]], [y1[frame]])
    m2_dot.set_data([x2[frame]], [y2[frame]])
    
    # Update trails with proper spacing for smooth ellipse
    trail_step = max(1, frame//50)  # Dynamic step for smooth ellipse
    m1_trail.set_data(x1[:frame+1:trail_step], y1[:frame+1:trail_step])
    m2_trail.set_data(x2[:frame+1:trail_step], y2[:frame+1:trail_step])
    
    return m1_dot, m2_dot, m1_trail, m2_trail

# Create animation
ani = FuncAnimation(
    fig, 
    update, 
    frames=len(t), 
    init_func=init,
    interval=20,  # Balanced speed
    blit=True
)

# Save as GIF
print("Creating elliptical orbit animation...")
ani.save('elliptical_orbit.gif', 
         writer=PillowWriter(fps=25),
         dpi=100,
         progress_callback=lambda i, n: print(f"Saving frame {i}/{n}") if i % 50 == 0 else None)
print("Animation saved as elliptical_orbit.gif")
plt.close()