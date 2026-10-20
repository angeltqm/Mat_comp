import sys

TOL = 1e-10

def leer_matriz(ruta):
    try:
        with open(ruta, "r") as f:
            lineas = [l.split() for l in f if l.strip()]
            n = int(lineas[0][0])
            matriz = [[float(x) for x in lineas[i+1]] for i in range(n)]
            if any(len(fila) != n+1 for fila in matriz):
                raise ValueError("Cada fila debe tener n+1 valores")
            return n, matriz
    except FileNotFoundError:
        sys.exit("Error: no existe el archivo")
    except (ValueError, IndexError) as e:
        sys.exit("Error de formato")

def gauss_jordan(a,n):
    for j in range(n):
        fila_piv = j
        for i in range(j + 1,n):
            if abs(a[i][j] > abs(a[fila_piv][j])):
                fila_piv = i

        if abs(a[fila_piv][j]) < TOL:
            return False

        if fila_piv != j:
            a[j], a[fila_piv] = a[fila_piv], a[j]

        piv = a[j][j]
        for k in range(n+1):
            a[j][k]/=piv

        for i in range(n):
            if i !=j:
                factor = a[i][j]
                for k in range(n+1):
                    a[i][k] -= factor * a[j][k]
    return True

def main():
    ruta = sys.argv[1] if len(sys.argv) > 1 else "matriz_prueba_3.txt"
    n, original = leer_matriz(ruta)
    a = [fila[:] for fila in original]

    if not gauss_jordan(a,n):
        print("No se pudo obtener una solucion")
        return

    x = [a[i][n] for i in range(n)]
    for i, xi in enumerate(x, 1):
        print(f"x{i} = {xi:.2f}" if n <= 10 else f"P{i:03d} = {xi:.2f}")

    error_max = max(
        abs(sum(original[i][k] * x[k] for k in range(n)) - original[i][n])
        for i in range(n)
    )
    print(f"\nError maximo: {error_max:.3e}")

if __name__ == "__main__":
    main()