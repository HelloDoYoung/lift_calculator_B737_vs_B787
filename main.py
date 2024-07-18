import numpy as np
import matplotlib.pyplot as plt

rho = 1.225
mps_to_knots = 1.94384

aircrafts = {
    'B787': {'wing_area': 325, 'cl': 0.11837},
    'B737': {'wing_area': 125, 'cl': 0.14035}
}

velocity_mps = np.linspace(150, 180, 200)
velocity_knots = velocity_mps * mps_to_knots

plt.figure(figsize=(10, 6))

for aircraft, specs in aircrafts.items():
    wing_area = specs['wing_area']
    cl = specs['cl']
    lift = 0.5 * rho * (velocity_mps ** 2) * wing_area * cl
    plt.plot(velocity_knots, lift, label=aircraft)

plt.title('Lift vs Velocity for B787 and B737')
plt.xlabel('Velocity (knots)')
plt.ylabel('Lift (N)')
plt.legend()
plt.grid(True)
plt.show()
