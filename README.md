# Math Modeling: Stability and Bifurcation of a Simple Food Chain in a Chemostat

This repository contains the source code, experimental notebooks, and documentation for a mathematical modeling project based on the paper **"Stability and bifurcation of a simple food chain in a chemostat with removal rates."**

## Project Structure

The project is organized into the following main directories:

- **`code/`**: Contains the core Python implementation of the mathematical models.
  - `model.py`: Defines the `ChemostatModel` class, including functional responses, the ODE system representing the food chain ($S, x, y, z$), numerical equilibrium solvers, Jacobian matrix computation, eigenvalue analysis, and Hopf bifurcation detection.
  - `simulation.py`: Functions for simulating the ODE system over time.
  - `equilibria.py`, `classification.py`: Modules for analyzing the boundary and interior equilibria.
  - `plotting.py`: Utilities for visualizing the simulation results and phase diagrams.
  - `run.py`: A simple script to run the basic model and check for Hopf bifurcations.
  - `utils.py`: General utility functions.

- **`experiments/`**: Contains Jupyter notebooks that walk through the analysis and generate figures for the report.
  - `01_basic_properties_and_boundary_equilibria.ipynb`: Analysis of basic properties and boundary equilibria.
  - `02_persistence_and_lyapunov.ipynb`: Studies on system persistence and Lyapunov stability.
  - `03_hopf_bifurcation.ipynb`: Detection and analysis of Hopf bifurcations in the system.
  - `04_hopf_bifurcation_P3.ipynb`: Further analysis of Hopf bifurcations.
  - `05_removal_rate_phase_diagram.ipynb`: Generates phase diagrams based on removal rates.
  - `figures/`: Directory where generated plots are saved.

- **`Population dynamics/`**: Contains the reference paper, *Stability and bifurcation of a simple food chain in a chemostat with removal rates.pdf*.

- **`report.pdf`** & **`Slide.pdf`**: The final project report and presentation slides detailing the findings and analysis.

## Getting Started

### Prerequisites

The code requires Python 3 and the following scientific computing libraries:
- `numpy`
- `scipy`
- `matplotlib`
- `jupyter` (for running the notebooks)

You can install the dependencies using pip:
```bash
pip install numpy scipy matplotlib jupyter
```

### Running the Code

1. **Basic Execution**: You can test the core model by running the `run.py` script:
   ```bash
   cd code
   python run.py
   ```

2. **Jupyter Notebooks**: To view the full analysis and generate figures, start Jupyter Notebook in the `experiments/` directory:
   ```bash
   cd experiments
   jupyter notebook
   ```
   Then, open any of the `.ipynb` files to run the interactive experiments.

## License

This project was developed for a Math Modeling course. Please refer to the authors for usage and permissions.
