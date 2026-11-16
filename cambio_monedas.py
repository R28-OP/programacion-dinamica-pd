def calcular_cambio_minimo(monedas: list[int], objetivo: int):
    """
    Encuentra la cantidad mínima de monedas para formar 'objetivo'
    y reconstruye la combinación exacta usada.
    """
    if objetivo < 0:
        raise ValueError("La cantidad objetivo debe ser mayor o igual a cero.")

    infinito = objetivo + 1
    dp = [infinito] * (objetivo + 1)
    dp[0] = 0  # Caso base: 0 monedas para monto 0

    # Arreglo para rastrear qué moneda generó cada estado óptimo
    ultima_moneda = [-1] * (objetivo + 1)

    for i in range(1, objetivo + 1):
        for moneda in monedas:
            if moneda <= i and dp[i - moneda] + 1 < dp[i]:
                dp[i] = dp[i - moneda] + 1
                ultima_moneda[i] = moneda

    if dp[objetivo] == infinito:
        return -1, [], dp

    # Reconstrucción de las monedas utilizadas desde el objetivo hacia 0
    combinacion = []
    monto_actual = objetivo
    while monto_actual > 0:
        moneda = ultima_moneda[monto_actual]
        combinacion.append(moneda)
        monto_actual -= moneda

    combinacion.sort(reverse=True)
    return dp[objetivo], combinacion, dp


if __name__ == "__main__":
    print("--- PROBLEMA 2: CAMBIO MÍNIMO DE MONEDAS ---")
    try:
        datos = input("Ingrese las denominaciones separadas por espacio (ej. 1 3 4): ")
        monedas = [int(m) for m in datos.strip().split()]
        objetivo = int(input("Ingrese la cantidad objetivo: "))

        minimo, combinacion, tabla_dp = calcular_cambio_minimo(monedas, objetivo)

        if minimo == -1:
            print(f"\nNo es posible formar {objetivo} con las denominaciones dadas.")
        else:
            print(f"\nCantidad mínima de monedas: {minimo}")
            print(f"Combinación: {' + '.join(map(str, combinacion))}")
            print(f"Tabla DP:\n{tabla_dp}")
    except ValueError:
        print("Entrada inválida: ingrese únicamente números enteros.")
