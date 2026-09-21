import math
def f(x):
    return 8 * math.sin(x) * math.exp(-x) - 1

def regla_falsa(xi, xf, tol=0.1, max_iter=100):
    if f(xi) * f(xf) >=0:
        return None

    xr_anterior = None
    print(f"{'Iter':<5}{'xi':<12}{'xf':<12}{'xr':<12}{'f(xr)':<14}{'error %':<10}")

    for i in range (1, max_iter +1 ):
        fxi = f(xi)
        fxf = f(xf)
        xr = xf - fxf * (xi - xf) / (fxi - fxf)
        fxr = f(xr)

        #Error aproximado
        if xr_anterior is None:
            error = None
            print(f"{i:<5}{xi:<12.4f}{xf:<12.4f}{xr:<12.4f}{fxr:<14.4f}{'---':<10}")
        else: 
            error = abs((xr - xr_anterior)/xr) * 100
            print(f"{i:<5}{xi:<12.4f}{xf:<12.4f}{xr:<12.4f}{fxr:<14.4f}{error:<10.4f}")

        #Criterio de parada
        if error is not None and error < tol:
            print(f"\nRaíz aproximada: x = {xr:.4f}  (error = {error:.4f}% < {tol}%)")
            return xr

        #Decidir en que subintervalo sigue la raiz
        if fxi * fxr <0:
            xf = xr
        else:
            xi = xr
        xr_anterior = xr

    print("Se alcanzo el maximo de iteraciones sin cumplir el criterio")
    return xr

# Valores iniciales
raiz = regla_falsa (xi=0.0, xf=1.0, tol=0.1)