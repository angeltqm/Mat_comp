import math

#Problema 1
def f1(x):
    return x**4 - 8*x**3 - 35*x**2 + 450*x - 1001

#Problema 2
def f2(x):
    return 8 * math.sin(x) * math.exp(-x) - 1

#xi: Valor inicial
#xf: Valor final
#eamax: Error aproximado maximo

def regla_falsa(f, xi, xf, eamax, max_iter=100):
    if f(xi) * f(xf) >= 0:
        raise ValueError("El intervalo no encierra una raíz (no hay cambio de signo)")


    yi = f(xi)
    yf = f(xf)
    xr = xi - (xf - xi) * yi / (yf - yi)

    for iteracion in range (1, max_iter +1 ):
        yr = f(xr)
        if yi * yr < 0.0:
            xf = xr
        elif yi * yr > 0.0:
            xi = xr
        else:
            return xr


        xrv = xr
        yi = f(xi)
        yf = f(xf)
        xr = xi - (xf - xi) * yi / (yf - yi)

        ea = abs((xr - xrv) / xr)*100
        print(f"{iteracion:>3} xr = {xr:.4f}  ea = {ea:.4f}%")

        if ea <= eamax:
            return xr

    raise RuntimeError("No convergio en max_iter iteraciones")

print("--------------Problema 1------------------")
raiz1 = regla_falsa(f1, 5.0, 6.0, 0.1)
print(f"Raiz aproximada: {raiz1:.4f}\n")

print("--------------Problema 2------------------")
raiz2 = regla_falsa(f2, 0.0, 1.0, 0.1)
print(f"Raiz aproximada: {raiz2:.4f}\n")