"""Shell Sort - Ordenamiento de Shell.
Usa brechas para ordenar elementos lejanos antes de hacer una inserción final.
"""

from typing import List


def shell_sort(arr: List[int]) -> List[int]:
    """Retorna una lista ordenada usando Shell Sort."""
    nums = arr.copy()
    n = len(nums)
    gap = n // 2

    # Reducir el gap hasta llegar a 1.
    while gap > 0:
        for i in range(gap, n):
            temp = nums[i]
            j = i
            # Comparar elementos separados por el gap y desplazar si están fuera de orden.
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
        gap //= 2

    return nums


def main() -> None:
    ejemplo = [23, 12, 1, 8, 34, 54, 2, 3]
    print('Shell Sort')
    print('Entrada:', ejemplo)
    resultado = shell_sort(ejemplo)
    print('Salida ordenada:', resultado)
    print('Explicación: usa brechas más grandes al principio y las reduce hasta ordenar con inserción.')


if __name__ == '__main__':
    main()
