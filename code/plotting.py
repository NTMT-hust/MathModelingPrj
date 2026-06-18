import numpy as np
import matplotlib.pyplot as plt

def plot_timeseries(sol, title):
    t = np.linspace(sol.t[0], sol.t[-1], 2000)
    S, x, y, z = sol.sol(t)
    plt.figure()
    for arr, label in [(S, "S nutrient"), (x, "x prey"), (y, "y predator 1"), (z, "z predator 2")]:
        plt.plot(t, arr, label=label)
    plt.xlabel("time")
    plt.ylabel("state")
    plt.title(title)
    plt.legend()
    plt.show()
    return t, S, x, y, z
