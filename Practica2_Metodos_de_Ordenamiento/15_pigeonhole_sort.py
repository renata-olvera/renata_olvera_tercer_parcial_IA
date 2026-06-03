"""Pigeonhole Sort - Ordenamiento por casilleros.
Funciona bien cuando los valores están dentro de un rango pequeño.
"""

from typing import List


def pigeonhole_sort(arr: List[int]) -> List[int]:
    """Retorna una lista ordenada usando Pigeonhole Sort."""
    if not arr:
        return []

    minimo = min(arr)
    maximo = max(arr)
    size = maximo - minimo + 1
    holes = [0] * size

    # Contar cuántos elementos caen en cada casillero.
    for num in arr:
        holes[num - minimo] += 1

    salida = []
    # Reconstruir la lista ordenada a partir de los casilleros.
    for i in range(size):
        salida.extend([i + minimo] * holes[i])

    return salida


def main() -> None:
    ejemplo = [8, 3, 2, 7, 4, 6, 8]
    print('Pigeonhole Sort')
    print('Entrada:', ejemplo)
    resultado = pigeonhole_sort(ejemplo)
    print('Salida ordenada:', resultado)
    print('Explicación: dispensa valores en casilleros y reconstruye el arreglo usando sus frecuencias.')


if __name__ == '__main__':
    main()
