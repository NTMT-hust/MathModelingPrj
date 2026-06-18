from model import *

params = {
    'a1': 2.0, 'b1': 0.5,
    'a2': 1.5, 'b2': 0.3,
    'a3': 1.2, 'b3': 0.2,
    'D1': 0.4,
    'D2': 0.3,
    'D3': 0.2
}

model = ChemostatModel(params)

eq = model.equilibrium([0.5,0.5,0.3,0.2])

print("Equilibrium:")
print(eq)

eigs = model.eigen_analysis(eq)

print("Eigenvalues:")
print(eigs)

if model.detect_hopf(eigs):
    print("Hopf bifurcation detected")
else:
    print("No Hopf bifurcation")