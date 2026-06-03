"""Counting Sort - Ordenamiento por conteo.
Cuenta la frecuencia de cada valor dentro de un rango conocido.
"""

from typing import List


def counting_sort(arr: List[int]) -> List[int]:
    """Retorna una lista ordenada usando Counting Sort."""
    if not arr:
        return []

    # Encontrar el rango de valores para construir el arreglo de conteo.
    minimo = min(arr)
    maximo = max(arr)
    rango = maximo - minimo + 1

    contador = [0] * rango

    # Contar cuántas veces aparece cada elemento.
    for num in arr:
        contador[num - minimo] += 1

    # Convertir el conteo en posiciones acumuladas.
    for i in range(1, rango):
        contador[i] += contador[i - 1]

    salida = [0] * len(arr)

    # Colocar cada elemento en su posición correcta dentro del arreglo de salida.
    for num in reversed(arr):
        index = num - minimo
        salida[contador[index] - 1] = num
        contador[index] -= 1

    return salida


def main() -> None:
    ejemplo = [4, 2, 2, 8, 3, 3, 1]
    print('Counting Sort')
    print('Entrada:', ejemplo)
    resultado = counting_sort(ejemplo)
    print('Salida ordenada:', resultado)
    print('Explicación: cuenta ocurrencias y reconstruye el arreglo en orden ascendente.')


if __name__ == '__main__':
    main()
