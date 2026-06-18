import numpy as np
from scipy.integrate import solve_ivp
from model import ChemostatModel

def simulate(p, U0=(0.8, 0.2, 0.1, 0.05), T=250, max_step=0.05):
    return solve_ivp(lambda t, U: ChemostatModel(p).system(U), (0, T), U0, dense_output=True, max_step=max_step, rtol=1e-8, atol=1e-10)

def solve_model(p, U0=(0.85, 0.30, 0.12, 0.05), T=180.0, transient=100.0, n_eval=180, max_step=0.75):
    t_eval = np.linspace(transient, T, n_eval)
    sol = solve_ivp(
        lambda t, U: ChemostatModel(p).system(np.maximum(U, 0.0)),
        (0.0, T),
        U0,
        t_eval=t_eval,
        max_step=max_step,
        rtol=1e-5,
        atol=1e-8,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.t, np.maximum(sol.y, 0.0)
