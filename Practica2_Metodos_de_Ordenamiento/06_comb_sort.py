"""Comb Sort - Ordenamiento tipo peine.
Mejora el Bubble Sort usando brechas más grandes al inicio.
"""

from typing import List


def comb_sort(arr: List[int]) -> List[int]:
    """Retorna una lista ordenada usando Comb Sort."""
    nums = arr.copy()
    n = len(nums)
    gap = n
    shrink = 1.3
    sorted_flag = False

    # El ciclo continúa hasta que el arreglo está ordenado y el gap es 1.
    while not sorted_flag:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted_flag = True

        # Comparar pares separados por el gap actual.
        i = 0
        while i + gap < n:
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                sorted_flag = False
            i += 1

    return nums


def main() -> None:
    ejemplo = [8, 4, 1, 56, 3, -44, 23, -6, 28, 0]
    print('Comb Sort')
    print('Entrada:', ejemplo)
    resultado = comb_sort(ejemplo)
    print('Salida ordenada:', resultado)
    print('Explicación: usa un gap decreciente para comparar elementos distantes antes de hacer intercambios cercanos.')


if __name__ == '__main__':
    main()
