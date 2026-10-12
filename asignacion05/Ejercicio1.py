import math

#Problema 1
def f1(x):
    return x**4 - 8*x**3 - 35*x**2 + 450*x - 1001

def df1(x):
    return 4*x**3 - 24*x**2 - 70*x + 450

#Problema 2
def f2(x):
    return 8 * math.sin(x) * math.exp(-x) - 1

def newton_raphson(f, df, x0, eamax, max_iter=100):
    xr = x0
    print(f"{'it':>3} {'xr':>12} {'f(xr)':>14} {'ea (%)':>10}")
    for i in range(1, max_iter + 1):
        derivada = df(xr)
        if derivada == 0:
            raise ZeroDivisionError("La derivada es 0, el método no puede continuar")

        xrv = xr
        xr = xrv - f(xrv) / derivada
        ea = abs((xr - xrv) / xr) * 100

        print(f"{i:>3} {xr:>12.4f} {f(xr):>14.4f} {ea:>10.4f}")

        if ea <= eamax:
            return xr
    raise RuntimeError("No se convergio en max_iter iteraciones")

def secante(f, x1, x2, eamax, max_iter=100):
    print(f"{'it':>3} {'xr':>12} {'f(xr)':>14} {'ea (%)':>10}")
    for i in range(1, max_iter + 1):
        f1_ = f(x1)
        f2_ = f(x2)
        if f1_ - f2_ == 0:
            raise ZeroDivisionError("f(x1) = f(x2), el metodo no puede continuar")

        xr = x2 - f2_ * (x1 - x2) / (f1_ - f2_)
        ea = abs((xr - x2) / xr) * 100

        print(f"{i:>3} {xr:>12.4f} {f(xr):>14.4f} {ea:>10.4f}")

        if ea <= eamax:
            return xr

        x1 = x2
        x2 = xr
    raise RuntimeError("No convergio en max_iter iteraciones")


print("--------------Problema 1 (Newton-Raphson)------------------")
raiz1 = newton_raphson(f1, df1, -7.0, 0.1)
print(f"Raiz aproximada: {raiz1:.4f}\n")

print("--------------Problema 2 (Secante)------------------")
raiz2 = secante(f2, 0.0, 1.0, 0.1)
print(f"Raiz aproximada: {raiz2:.4f}\n")