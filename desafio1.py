import numpy as np

A = np.array([
    [52, 30, 18],  # Cantera 1
    [20, 50, 30],  # Cantera 2
    [25, 20, 55]   # Cantera 3
]) / 100

B = np.array([4800, 5810, 5690])

A_inv = np.linalg.inv(A)

X = np.dot(A_inv, B)

print("Cantidad de material que se debe transportar de cada cantera (m^3):")
print(f"Cantera 1: {X[0]:.2f} m³")
print(f"Cantera 2: {X[1]:.2f} m³")
print(f"Cantera 3: {X[2]:.2f} m³")
