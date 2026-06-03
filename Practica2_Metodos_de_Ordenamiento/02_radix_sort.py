"""Radix Sort - Ordenamiento por dígitos.
Ordena números enteros usando la posición de cada dígito en base 10.
"""

from typing import List


def counting_sort_for_radix(arr: List[int], exp: int) -> List[int]:
    """Ordena la lista según el dígito en la posición exp."""
    n = len(arr)
    salida = [0] * n
    contador = [0] * 10

    # Contar cuántos números tienen cada valor en el dígito actual.
    for num in arr:
        index = (num // exp) % 10
        contador[index] += 1

    # Convertir el conteo en posiciones acumuladas.
    for i in range(1, 10):
        contador[i] += contador[i - 1]

    # Construir el arreglo ordenado por el dígito actual.
    for num in reversed(arr):
        index = (num // exp) % 10
        salida[contador[index] - 1] = num
        contador[index] -= 1

    return salida


def radix_sort(arr: List[int]) -> List[int]:
    """Retorna una lista ordenada usando Radix Sort."""
    if not arr:
        return []

    nums = arr.copy()
    maximo = max(nums)
    exp = 1

    # Ordenar por cada dígito, de menos significativo a más significativo.
    while maximo // exp > 0:
        nums = counting_sort_for_radix(nums, exp)
        exp *= 10

    return nums


def main() -> None:
    ejemplo = [170, 45, 75, 90, 802, 24, 2, 66]
    print('Radix Sort')
    print('Entrada:', ejemplo)
    resultado = radix_sort(ejemplo)
    print('Salida ordenada:', resultado)
    print('Explicación: ordena por cada dígito comenzando con el menos significativo.')


if __name__ == '__main__':
    main()
