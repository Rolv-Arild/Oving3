from sympy import symbols, Matrix, sqrt

sym = x, y = symbols('x y', real=True)

c1 = x1, y1 = 0, 1
c2 = x2, y2 = 1, 1
c3 = x3, y3 = 0, -1

c = c1, c2, c3
radii = [1] * len(c)

fun = r1, r2, r3 = sqrt((x - x1) ** 2 + (y - y1) ** 2) - radii[0], \
                   sqrt((x - x2) ** 2 + (y - y2) ** 2) - radii[1], \
                   sqrt((x - x3) ** 2 + (y - y3) ** 2) - radii[2]

xk = Matrix(len(sym), 1, [0] * len(sym))


def S(n):
    return fun[n].subs([(x, xk[0]), (y, xk[1])]).evalf() + radii[n]


def Dr():
    return Matrix(len(fun), len(sym), lambda j, i: (xk[i] - c[j][i]) / (S(j)))


def r():
    return Matrix(len(fun), 1, lambda j, i: fun[j].subs([(x, xk[0]), (y, xk[1])]).evalf())


for k in range(0, 20):
    A = Dr()
    v = (A.transpose() * A).LUsolve(-A.transpose() * r())
    xk = xk + v

print("(x, y)=(%f, %f)" % (xk[0], xk[1]))
