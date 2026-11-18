"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: write k_imbalance(x) = (2x)^2/((a-x)(b-x)) - K.
#         It equals zero exactly at equilibrium.
def k_imbalance(x):
   return np.pow(2*x,2)/((a-x)*(b-x)) - K

# TODO 2 (method 1): use scipy.optimize.newton to find the root of k_imbalance
#         (start x0=0.5). This is root-finding.
root_bynewton = newton(k_imbalance, x0=0.5)

print("Equilibrium extent (Mehtode1 - newton):", root_bynewton)

# TODO 3 (method 2): use scipy.optimize.minimize to minimise k_imbalance(x)**2
#         (method "SLSQP", bounds [(0, 0.999)], x0=[0.5]). Print both answers
#         and confirm they agree.
def error(x):
    return k_imbalance(x[0])**2
result = minimize(
    error,
    x0=[0.5],
    method="SLSQP",
    bounds=[(0, 0.999)]
)

x_slsqp = result.x[0]

print("Equilibrium extent (SLSQP):", x_slsqp)
print("Difference:", abs(root_bynewton - x_slsqp))


# TODO 4: report the equilibriumuilibrium amounts (H2, I2, HI), and plot how the three
#         amounts change with the extent x, marking the equilibrium. Save
#         equilibrium.png.

H2_eq= a - root_bynewton
I2_eq = b - root_bynewton
HI_eq = 2*root_bynewton

print("H2 at equilibrium:", H2_eq)
print("I2 at equilibrium:", I2_eq)
print("HI at equilibrium:", HI_eq)

#Ploting three amounts change with extnet x
x_values = np.linspace(0, 1, 200)

H2 = a - x_values
I2 = b - x_values
HI = 2*x_values

plt.plot(x_values, H2, label="H2", color="blue")
plt.plot(x_values, I2, label="I2", color="green", linestyle="--")
plt.plot(x_values, HI, label="HI", color="red")

plt.axvline(root_bynewton, color="black",label="Equilibrium")

plt.xlabel("Reaction extent x (mol)")
plt.ylabel("Amount (mol)")
plt.title("Chemical Equilibrium")
plt.legend()
plt.grid(True)

plt.savefig("equilibrium.png")
plt.show()