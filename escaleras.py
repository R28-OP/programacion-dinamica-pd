def calcular_formas_escalera(n: int):
    """
    Calcula el total de formas distintas de subir N escalones
    dando pasos de 1 o 2 unidades mediante Programación Dinámica.
    """
    if n < 0:
        raise ValueError("El número de escalones no puede ser negativo.")
    if n == 0:
        return 1, [1]

    # Tabla DP donde dp[i] guarda las formas de llegar al escalón i
    dp = [0] * (n + 1)
    dp[0] = 1  # Caso base: 1 forma de quedarse en el inicio
    dp[1] = 1  # Caso base: 1 forma de subir al primer escalón

    # Construcción Bottom-Up de la tabla
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n], dp


if __name__ == "__main__":
    print("--- PROBLEMA 1: ESCALERAS ---")
    try:
        n = int(input("Ingrese el número de escalones (N): "))
        total_formas, tabla_dp = calcular_formas_escalera(n)
        print(f"\nFormas posibles: {total_formas}")
        print(f"Tabla DP:\n{tabla_dp}")
    except ValueError as error:
        print(f"Entrada inválida: {error}")
