# CSPC – Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
  conda env create -f PW<n>/Lab <X>/environment.yml
  conda activate cspc

---

## PW1 – Lab A: Reproducible Foundations

**What I built:**
- A decay simulation comparing Python loop against vectorized NumPy implementation, along with pytest test cases.

**Speed comparison (loop vs NumPy):**
- loop : 2.6712 s
- numpy : 0.0003 s
- speed-up: 8853.6x faster

**Tests:** all passing? yes 

**Conclusion:**
- Vectorising code using NumPy drastically improves computational performance by replacing standard Python loops with optimized C-level operations achieving an 8853.6x speedup. All unit tests pass, confirming that the vectorized simulation maintains complete accuracy while running much faster.

---

## PW2 — Lab A: Motion from Tracking Data

### Part 2 — From position to velocity and acceleration 
Results:

- Mean acceleration: -8.58 m/s²
- Standard deviation of acceleration: 28.72 m/s²

### Part 3 — The noise problem

The acceleration is very noisy because numerical differentiation amplifies
measurement noise. Since acceleration is obtained by differentiating the
position data twice, the noise becomes much larger.

### Part 4 — Integrating back

After integrating the noisy acceleration back to velocity and position,
the maximum difference between the recovered and original position is
approximately 0.785 m.

This shows that integration suppresses noise and can recover the original
position quite closely even from noisy acceleration data.


## PW1 — Lab B: Data Visualization and Automation

### Data analysis
Loaded observed decay data from decay_observed.csv and compared it
with the analytical exponential decay model:

N(t) = N0 * exp(-0.3 * t)

The observed data were plotted as scatter points, while the
analytical model was plotted as a continuous curve.

### Snakemake automation
Created a Snakefile to automate the generation of figure.png.

After deleting figure.png, Snakemake successfully regenerated it.

Running Snakemake again without changing the input files produced:
"Nothing to be done (all requested files are present and up to date)."

This demonstrates that Snakemake avoids unnecessary computations.


## PW2 — Lab B: Numerical Optimization

### Part 2A — Convex Function

All three methods (Gradient Descent, Newton, and SLSQP)
converged to x = 3, the minimum of f(x) = (x - 3)^2 + 1.

### Part 2B — Non-Convex Function

Gradient Descent and SLSQP converged to approximately
x = -1.30084 from both starting points.

Newton produced different stationary points:
- From x0 = 0, Newton found x = 0.16994.
  The second derivative is negative, so this is a local maximum.
- From x0 = 2, Newton found x = 1.13090.
  The second derivative is positive, so this is a local minimum.

Conclusion:
The methods do not always agree. Newton's method finds
stationary points, which are not necessarily minima.
The starting point can influence the result of optimization.

### Part 3 — Chemistry 1: fit a reaction rate

The fitted rate constant is k = 0.26176.

The fitted exponential curve follows the measured concentration
data closely. The result is close to the expected value of k = 0.25.

The optimization was performed using scipy.optimize.minimize
with the SLSQP method.

### Part 4 — Chemistry 2: chemical equilibrium

Studied the equilibrium reaction:

H2 + I2 ⇌ 2HI

The equilibrium extent was calculated using two numerical methods:
- Newton's method (`scipy.optimize.newton`) for root-finding.
- SLSQP (`scipy.optimize.minimize`) for minimizing the squared equilibrium imbalance.

**Results:**
- Newton: x = 0.66384767
- SLSQP: x = 0.66384743
- Difference: 2.39 × 10⁻⁷

**Equilibrium composition:**
- H2 = 0.33615 mol
- I2 = 0.33615 mol
- HI = 1.32770 molS

Both methods produced nearly identical results.

The amounts of H2, I2, and HI were plotted against the reaction extent, with the equilibrium position marked by a vertical line.

Output: `equilibrium.png`

### Part 5 (bonus) — Chemistry 3: titration equivalence point

Analyzed titration data from `titration.csv` to determine the equivalence point.

The numerical derivative of pH with respect to the volume of added base was calculated using `np.gradient()`.

The maximum slope was identified using `np.argmax()`.

**Results:**
- Equivalence point volume: V = 50
- Maximum slope: dpH/dV = 4.0

Two plots were generated:
- pH versus volume of added base, with the equivalence point marked.
- dpH/dV versus volume of added base, with the maximum slope highlighted.

Output: `titration.png`

### Conclusion

This lab demonstrated how numerical optimization and root-finding methods can be applied to mathematical and chemical problems.

Newton's method and SLSQP produced consistent results for chemical equilibrium, while numerical differentiation allowed the equivalence point of a titration curve to be identified.