import numpy as np
from sympy import Matrix, symbols, sqrt, ln, E

pop = np.array([[1960.0, 3039585530.0],
                [1970.0, 3707475887.0],
                [1990.0, 5281653820.0],
                [2000.0, 6079603571.0]])


def fill(i, j, t):
    if j == 0:
        return 1.0
    if j == 1:
        return pop[i][t]
    if j == 2:
        return pop[i][t] ** 2
    return pop[i][t] ** 3


# Line
A = Matrix(4, 2, lambda i, j: fill(i, j, 0))
b = Matrix(4, 1, [ln(p[1]) for p in pop])

b = A.transpose() * b
A = A.transpose() * A

exp = A.LUsolve(b)

x = symbols('x', real=True)

f = E ** exp[0, 0] * E ** (exp[1, 0] * x)

est = f.subs(x, 1980)
actual = 4452584592

print("Funksjon:", f)
print("1980: Estimert:", est, "Feil:", abs(est - actual))
