def f(x):
    return x**4 - 8*x**3 - 35*x**2 + 450*x - 1001

def biseccion(xi, xf, tol=0.1, max_iter=100):
    if f(xi) * f(xf) >=0:
        return None

    xr_anterior = None
    print(f"{'Iter':<5}{'xi':<12}{'xf':<12}{'xr':<12}{'f(xr)':<14}{'error %':<10}")

    for i in range (1, max_iter +1 ):
        xr = (xi + xf)/2
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
        if f(xi) * fxr <0:
            xf = xr
        else:
            xi = xr
        xr_anterior = xr

    print("Se alcanzo el maximo de iteraciones sin cumplir el criterio")
    return xr
# Valores iniciales
raiz = biseccion (xi=5.0, xf=6.0, tol=0.1)