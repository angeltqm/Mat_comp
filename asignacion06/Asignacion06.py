import random
import time


def gauss(matriz):
    
    n = len(matriz)

    for k in range(n):
        fila_max = max(range(k, n), key=lambda i: abs(matriz[i][k]))
        if abs(matriz[fila_max][k]) < 1e-12:
            raise ValueError("El sistema no tiene solución unica (pivote cero)")
        if fila_max != k:
            matriz[k], matriz[fila_max] = matriz[fila_max], matriz[k]

        fila_k = matriz[k]
        pivote = fila_k[k]

        for i in range(k + 1, n):
            fila_i = matriz[i]
            m = fila_i[k] / pivote
            if m != 0.0:
                for j in range(k, n + 1):
                    fila_i[j] -= m * fila_k[j]

    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        suma = 0.0
        for j in range(i + 1, n):
            suma += matriz[i][j] * x[j]
        x[i] = (matriz[i][n] - suma) / matriz[i][i]

    return x


def residuo_maximo(a_original, x):
    """Sustituye x en el sistema original y regresa el mayor error |Ax - b|."""
    n = len(a_original)
    peor = 0.0
    for i in range(n):
        s = sum(a_original[i][j] * x[j] for j in range(n))
        peor = max(peor, abs(s - a_original[i][n]))
    return peor


def capturar_manual(n):
    print(f"Escribe cada fila con {n + 1} numeros separados por espacio "
          f"({n} coeficientes y el termino independiente).")
    matriz = []
    for i in range(n):
        while True:
            try:
                fila = [float(v) for v in input(f"Fila {i + 1}: ").split()]
                if len(fila) != n + 1:
                    print(f"  Deben ser {n + 1} numeros.")
                    continue
                matriz.append(fila)
                break
            except ValueError:
                print("  Solo numeros.")
    return matriz


def generar_aleatoria(n):
    """Genera un sistema con solucion conocida (x_i = 1..n) para poder verificar."""
    matriz = []
    solucion = [float(i + 1) for i in range(n)]
    for _ in range(n):
        fila = [random.uniform(-10, 10) for _ in range(n)]
        b = sum(fila[j] * solucion[j] for j in range(n))
        fila.append(b)
        matriz.append(fila)
    return matriz


def main():
    print("=== Metodo de Gauss (eliminación gaussiana) NxN ===")
    print("1) Capturar el sistema a mano")
    print("2) Ejemplo 3x3 (2x+y-z=8, -3x-y+2z=-11, -2x+y+2z=-3)")
    print("3) Sistema aleatorio de tamaño N")
    opcion = input("Opción: ").strip()

    if opcion == "1":
        n = int(input("Numero de incognitas N: "))
        matriz = capturar_manual(n)
    elif opcion == "2":
        matriz = [
            [2, 1, -1, 8],
            [-3, -1, 2, -11],
            [-2, 1, 2, -3],
        ]
        matriz = [[float(v) for v in fila] for fila in matriz]
    elif opcion == "3":
        n = int(input("Numero de incognitas N: "))
        matriz = generar_aleatoria(n)
    else:
        print("Opcion no valida")
        return

    n = len(matriz)
    original = [fila[:] for fila in matriz]

    inicio = time.time()
    x = gauss(matriz)
    tiempo = time.time() - inicio

    if n <= 10:
        nombres = "XYZ" if n <= 3 else None
        for i, valor in enumerate(x):
            etiqueta = nombres[i] if nombres else f"x{i + 1}"
            print(f"{etiqueta} = {valor:.4f}")
    else:
        print(f"Sistema de {n}x{n} resuelto. Primeras 5 incognitas:")
        for i in range(5):
            print(f"x{i + 1} = {x[i]:.4f}")
        print("...")
        print(f"x{n} = {x[-1]:.4f}")

    print(f"\nError maximo al sustituir en el sistema original: {residuo_maximo(original, x):.2e}")
    print(f"Tiempo de calculo: {tiempo:.3f} s")


if __name__ == "__main__":
    main()