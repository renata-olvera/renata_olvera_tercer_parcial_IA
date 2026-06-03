"""Cocktail Sort - Ordenamiento de cóctel.
Una variación bidireccional de Bubble Sort.
"""

from typing import List


def cocktail_sort(arr: List[int]) -> List[int]:
    """Retorna una lista ordenada usando Cocktail Sort."""
    nums = arr.copy()
    start = 0
    end = len(nums) - 1
    swapped = True

    # Recorremos el arreglo en ambos sentidos para mover extremos.
    while swapped:
        swapped = False
        for i in range(start, end):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end - 1, start - 1, -1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

        start += 1

    return nums


def main() -> None:
    ejemplo = [5, 1, 4, 2, 8, 0, 2]
    print('Cocktail Sort')
    print('Entrada:', ejemplo)
    resultado = cocktail_sort(ejemplo)
    print('Salida ordenada:', resultado)
    print('Explicación: ordena hacia adelante y hacia atrás en cada ciclo.')


if __name__ == '__main__':
    main()
