import numpy as np
from simulation import solve_model

def classify_regime(Y, extinction_eps=2e-3, amplitude_eps=3e-2):
    means = Y.mean(axis=1)
    amps = Y.max(axis=1) - Y.min(axis=1)
    S_mean, x_mean, y_mean, z_mean = means
    bio_amp = float(np.max(amps[1:]))

    x_alive = x_mean >= extinction_eps
    y_alive = y_mean >= extinction_eps
    z_alive = z_mean >= extinction_eps

    if not x_alive and not y_alive and not z_alive:
        regime = 0
    elif x_alive and not y_alive:
        regime = 1
    elif x_alive and y_alive and not z_alive:
        regime = 2
    elif x_alive and y_alive and z_alive and bio_amp < amplitude_eps:
        regime = 3
    elif x_alive and y_alive and z_alive:
        regime = 4
    else:
        regime = 0 if not x_alive else 1

    return regime, means, amps, bio_amp

def simulate_and_classify(D2, D3, base_params):
    p = dict(base_params, D2=float(D2), D3=float(D3))
    t, Y = solve_model(p)
    regime, means, amps, bio_amp = classify_regime(Y)
    return regime, means, amps, bio_amp
