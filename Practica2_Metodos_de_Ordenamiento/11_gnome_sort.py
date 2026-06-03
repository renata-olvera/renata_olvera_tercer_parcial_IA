"""Gnome Sort - Ordenamiento gnomo.
Se mueve hacia adelante y hacia atrás intercambiando elementos fuera de orden.
"""

from typing import List


def gnome_sort(arr: List[int]) -> List[int]:
    """Retorna una lista ordenada usando Gnome Sort."""
    nums = arr.copy()
    index = 0

    # El "gnomo" avanza cuando el orden es correcto y retrocede cuando encuentra un error.
    while index < len(nums):
        if index == 0 or nums[index] >= nums[index - 1]:
            index += 1
        else:
            nums[index], nums[index - 1] = nums[index - 1], nums[index]
            index -= 1

    return nums


def main() -> None:
    ejemplo = [34, 2, 10, -9]
    print('Gnome Sort')
    print('Entrada:', ejemplo)
    resultado = gnome_sort(ejemplo)
    print('Salida ordenada:', resultado)
    print('Explicación: compara un elemento con el anterior y retrocede si están fuera de orden.')


if __name__ == '__main__':
    main()
