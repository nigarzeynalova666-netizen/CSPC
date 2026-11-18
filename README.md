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