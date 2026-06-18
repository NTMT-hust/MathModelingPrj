import numpy as np

def monod_inv(D, a, b):
    return b * D / (a - D)
