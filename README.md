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