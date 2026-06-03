"""Bubble Sort - Ordenamiento por burbuja.
Compara cada par de elementos adyacentes y los intercambia si están fuera de orden.
"""

from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """Retorna una nueva lista ordenada usando Bubble Sort."""
    nums = arr.copy()
    n = len(nums)

    # Hacemos tantas pasadas como elementos hay en la lista.
    for i in range(n):
        swap_occurred = False

        # Durante cada pasada, los elementos más grandes "burbujean" hacia el final.
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swap_occurred = True

        # Si no se intercambió nada en una pasada, el arreglo ya está ordenado.
        if not swap_occurred:
            break

    return nums


def main() -> None:
    ejemplo = [64, 34, 25, 12, 22, 11, 90]
    print('Bubble Sort')
    print('Entrada:', ejemplo)
    resultado = bubble_sort(ejemplo)
    print('Salida ordenada:', resultado)
    print('Explicación: cada pasada mueve los valores más grandes hacia el final del arreglo.')


if __name__ == '__main__':
    main()
