import numpy as np
from scipy.optimize import root, brentq
from model import ChemostatModel
from utils import monod_inv

def P2(p):
    x2 = monod_inv(p["D2"], p["a2"], p["b2"])
    def eq(S):
        return S + ChemostatModel(p).f1(S) * x2 - 1
    S2 = brentq(eq, 1e-8, 1.0)
    y2 = x2 * (ChemostatModel(p).f1(S2) - p["D1"]) / p["D2"]
    return np.array([S2, x2, y2, 0.0])

def find_P3_2D(p, guess=(0.25, 0.6)):
    y3 = monod_inv(p["D3"], p["a3"], p["b3"])
    def equations(V):
        S, x = V
        f1 = ChemostatModel(p).f1(S)
        f2 = ChemostatModel(p).f2(x)
        return [S + f1*x - 1, x*(f1-p["D1"]) - f2*y3]
    sol = root(equations, guess)
    if not sol.success:
        raise RuntimeError(sol.message)
    S3, x3 = sol.x
    z3 = y3 * (ChemostatModel(p).f2(x3) - p["D2"]) / p["D3"]
    return np.array([S3, x3, y3, z3])

def find_P3_4D(p, guess=(0.32, 0.87, 0.04, 0.12)):
    sol = root(lambda U: ChemostatModel(p).system(U), guess)
    if not sol.success or np.any(sol.x <= 0):
        raise RuntimeError(f"Could not find positive P3")
    return sol.x
