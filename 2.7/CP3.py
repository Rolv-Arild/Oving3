from sympy import symbols, diff, Matrix

# DF(x)s=-F(x)

sym = u, v = symbols('u v', real=True)

fun = f1, f2 = u ** 3 - v ** 3 + u, \
               u ** 2 + v ** 2 - 1

DF = Matrix(2, 2, lambda i, j: diff(fun[i], sym[j]))
F = Matrix([[f1], [f2]])
x = Matrix([[1.0], [1.0]])

for _ in range(0, 10):
    x += DF.LUsolve(-F).subs([(u, x[0, 0]), (v, x[1, 0])])

print(x)

print(F.subs([(u, x[0, 0]), (v, x[1, 0])]))
