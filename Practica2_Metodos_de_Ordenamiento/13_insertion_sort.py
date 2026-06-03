"""Insertion Sort - Ordenamiento por inserción.
Construye una lista ordenada insertando cada elemento en su posición correcta.
"""

from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    """Retorna una nueva lista ordenada usando Insertion Sort."""
    nums = arr.copy()

    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        # Mover elementos mayores que key hacia la derecha para dejar espacio.
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

    return nums


def main() -> None:
    ejemplo = [12, 11, 13, 5, 6]
    print('Insertion Sort')
    print('Entrada:', ejemplo)
    resultado = insertion_sort(ejemplo)
    print('Salida ordenada:', resultado)
    print('Explicación: cada elemento se inserta en su lugar dentro de la parte ordenada a la izquierda.')


if __name__ == '__main__':
    main()
