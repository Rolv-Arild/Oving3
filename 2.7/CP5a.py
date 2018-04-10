from sympy import symbols, diff, Matrix

# DF(x)s=-F(x)

sym = x, y, z = symbols('x y z', real=True)

fun = f1, f2, f3 = (x - 1) ** 2 + (y - 1) ** 2 + z ** 2 - 1, \
                   (x - 1) ** 2 + y ** 2 + (z - 1) ** 2 - 1, \
                   x ** 2 + (y - 1) ** 2 + (z - 1) ** 2 - 1

DF = Matrix(3, 3, lambda i, j: diff(fun[i], sym[j]))
F = Matrix([[f1], [f2], [f3]])
xn = Matrix([[0.0], [0.0], [0.0]])

for _ in range(0, 20):
    xn += DF.LUsolve(-F).subs([(x, xn[0, 0]), (y, xn[1, 0]), (z, xn[2, 0])])

print(xn)

print(F.subs([(x, xn[0, 0]), (y, xn[1, 0]), (z, xn[2, 0])]))

# Velger annet startpunkt for å finne punkt nr. 2
xn = Matrix([[10.0], [10.0], [10.0]])

for _ in range(0, 20):
    xn += DF.LUsolve(-F).subs([(x, xn[0, 0]), (y, xn[1, 0]), (z, xn[2, 0])])

print(xn)

print(F.subs([(x, xn[0, 0]), (y, xn[1, 0]), (z, xn[2, 0])]))
