"""Pancake Sort - Ordenamiento con volteos.
Ordena la lista usando la operación de voltear un prefijo del arreglo.
"""

from typing import List


def flip(arr: List[int], k: int) -> None:
    """Invierte el orden de los primeros k elementos del arreglo."""
    arr[:k] = reversed(arr[:k])


def pancake_sort(arr: List[int]) -> List[int]:
    """Retorna una lista ordenada usando Pancake Sort."""
    nums = arr.copy()
    n = len(nums)

    # Mover el elemento más grande al final una y otra vez.
    for curr_size in range(n, 1, -1):
        max_index = nums.index(max(nums[:curr_size]))

        # Si el máximo ya está en su posición final, no hacemos nada.
        if max_index != curr_size - 1:
            # Voltear el máximo al principio.
            if max_index != 0:
                flip(nums, max_index + 1)
            # Voltear el prefijo completo para llevar el máximo al final.
            flip(nums, curr_size)

    return nums


def main() -> None:
    ejemplo = [3, 6, 1, 10, 2, 5]
    print('Pancake Sort')
    print('Entrada:', ejemplo)
    resultado = pancake_sort(ejemplo)
    print('Salida ordenada:', resultado)
    print('Explicación: lleva el elemento más grande al final usando "flips" sucesivos.')


if __name__ == '__main__':
    main()
