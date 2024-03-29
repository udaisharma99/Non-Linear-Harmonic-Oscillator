# Non-Linear-Harmonic-Oscillator

This project was conducted as part of the PS-530 module of Computational Physics at Dublin City University. The project aimed to extend a linear simple harmonic motion solver to a nonlinear harmonic oscillator by introducing a nonlinear correction term and validate its accuracy using the Method of Manufactured Solutions. Additionally, the project explored the surprising loss of accuracy observed under certain conditions and sought to understand its underlying causes. The project was divided into two main phases.

The Methodology behind the 2 phases is given as follows:

Part I:

1. A linear simple harmonic motion solver was extended to a nonlinear harmonic oscillator by introducing a nonlinear correction term.
2. The solver's accuracy was assessed using a model called Method of Manufactured Solutions.
3. A manufactured term was added to the nonlinear harmonic oscillator's equation of motion.
4. The computer code was tested to determine if it correctly converged to the manufactured solution.
5. After verification, we turn off the manufactured solution knowing that if the solver is correct with the manufactured term, it will also be correct with the manufactured term omitted.

Part II:

1. Once the solver was verified, its performance was investigated under different conditions.
2. The effect of varying the nonlinear constant was analyzed.
3. A surprising loss of accuracy was observed as the nonlinear constant increased.
4. The cause of this loss was explored, and a plausible explanation was provided.

Learnings:
- Verification of Code by comparison with exact solutions: The preferred method whenever possible
- Convergence of the L2 relative error norm at an expected rate is the strongest test
- Use of Manufactured Solutions is often possible when no other exact solution is available
- Verification of Calculations is always necessary. Correct code does not guarantee correct solutions

This project leveraged the following skills:
1. Jupyter Notebook
2. Python
3. MMS Model
4. Numerical modelling
5. Model Validation
6. Model testing
7. Qualitative analysis
8. Data visualisation


The project concluded by successfully extending a linear harmonic oscillator solver to a nonlinear counterpart, validating its accuracy using a rigorous method, and identifying the reason behind the loss of accuracy under specific conditions.
