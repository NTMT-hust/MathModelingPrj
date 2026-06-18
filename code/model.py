import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
from numpy.linalg import eigvals

class ChemostatModel:

    def __init__(self, params):
        self.params = params

    # ----------------------------
    # Functional responses
    # ----------------------------

    def f1(self, S):
        a1, b1 = self.params['a1'], self.params['b1']
        return a1 * S / (b1 + S)

    def f2(self, x):
        a2, b2 = self.params['a2'], self.params['b2']
        return a2 * x / (b2 + x)

    def f3(self, y):
        a3, b3 = self.params['a3'], self.params['b3']
        return a3 * y / (b3 + y)

    # Derivatives of fi
    def df1(self, S):
        a1, b1 = self.params['a1'], self.params['b1']
        return a1 * b1 / (b1 + S)**2

    def df2(self, x):
        a2, b2 = self.params['a2'], self.params['b2']
        return a2 * b2 / (b2 + x)**2

    def df3(self, y):
        a3, b3 = self.params['a3'], self.params['b3']
        return a3 * b3 / (b3 + y)**2

    # ----------------------------
    # ODE system
    # ----------------------------

    def system(self, state):
        S, x, y, z = state
        D1, D2, D3 = self.params['D1'], self.params['D2'], self.params['D3']

        dS = 1 - S - self.f1(S) * x
        dx = x * (self.f1(S) - D1) - self.f2(x) * y
        dy = y * (self.f2(x) - D2) - self.f3(y) * z
        dz = z * (self.f3(y) - D3)

        return np.array([dS, dx, dy, dz])

    # ----------------------------
    # Find equilibrium numerically
    # ----------------------------

    def equilibrium(self, guess):
        eq = fsolve(self.system, guess)
        return eq

    # ----------------------------
    # Jacobian matrix
    # ----------------------------

    def jacobian(self, state):

        S, x, y, z = state
        D1, D2, D3 = self.params['D1'], self.params['D2'], self.params['D3']

        J = np.zeros((4,4))

        # Row 1
        J[0,0] = -1 - self.df1(S)*x
        J[0,1] = -self.f1(S)

        # Row 2
        J[1,0] = x * self.df1(S)
        J[1,1] = self.f1(S) - D1 - self.df2(x)*y
        J[1,2] = -self.f2(x)

        # Row 3
        J[2,1] = y * self.df2(x)
        J[2,2] = self.f2(x) - D2 - self.df3(y)*z
        J[2,3] = -self.f3(y)

        # Row 4
        J[3,2] = z * self.df3(y)
        J[3,3] = self.f3(y) - D3

        return J

    # ----------------------------
    # Eigenvalue analysis
    # ----------------------------

    def eigen_analysis(self, equilibrium):

        J = self.jacobian(equilibrium)

        eigs = eigvals(J)

        return eigs

    # ----------------------------
    # Hopf detection
    # ----------------------------

    def detect_hopf(self, eigs, tol=1e-3):

        for lam in eigs:

            # complex pair with near-zero real part
            if abs(np.real(lam)) < tol and abs(np.imag(lam)) > tol:
                return True

        return False