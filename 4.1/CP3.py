import numpy as np
from sympy import Matrix, symbols, sqrt

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
b = Matrix(4, 1, pop[:, 1])

b = A.transpose() * b
A = A.transpose() * A

line = A.LUsolve(b)

# Parabola
A = Matrix(4, 3, lambda i, j: fill(i, j, 0))
b = Matrix(4, 1, pop[:, 1])

b = A.transpose() * b
A = A.transpose() * A

par = A.LUsolve(b)

# Cubic
A = Matrix(4, 4, lambda i, j: fill(i, j, 0))
b = Matrix(4, 1, pop[:, 1])

b = A.transpose() * b
A = A.transpose() * A

cube = A.LUsolve(b)

x = symbols('x', real=True)

line = line[0, 0] + line[1, 0] * x
par = par[0, 0] + par[1, 0] * x + par[2, 0] * x ** 2
cube = cube[0, 0] + cube[1, 0] * x + cube[2, 0] * x ** 2 + cube[3, 0] * x ** 3

print("Linje:", line)
print("Parabel:", par)
print("Kubisk:", cube)

# RMSE line
RMSE = 0
for p in pop:
    RMSE += (line.subs(x, p[0]) - p[1]) ** 2
RMSE = sqrt(RMSE / len(pop))
print("RMSE linje: ", RMSE)

# RMSE parabola
RMSE = 0
for p in pop:
    RMSE += (par.subs(x, p[0]) - p[1]) ** 2
RMSE = sqrt(RMSE / len(pop))
print("RMSE parabel: ", RMSE)

# RMSE cubic
RMSE = 0
for p in pop:
    RMSE += (cube.subs(x, p[0]) - p[1]) ** 2
RMSE = sqrt(RMSE / len(pop))
print("RMSE kubisk: ", RMSE)

# 1980 population
actual = 4452584592

est = line.subs(x, 1980), par.subs(x, 1980), cube.subs(x, 1980)

print("1: 1980 linje:", est[0], ", feil:", abs(est[0] - actual))
print("2: 1980 parabel:", est[1], ", feil:", abs(est[1] - actual))
print("3: 1980 kubisk:", est[2], ", feil:", abs(est[2] - actual))
print("Beste:", [abs(actual - e) for e in est].index(min([abs(actual - e) for e in est])) + 1)
