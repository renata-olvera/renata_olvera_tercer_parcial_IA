"""Tim Sort - Ordenamiento híbrido inspirado en Python.
Combina insertion sort para segmentos pequeños y merge sort para mezclarlos.
"""

from typing import List


def insertion_sort_range(nums: List[int], left: int, right: int) -> None:
    """Ordena un rango pequeño del arreglo usando Insertion Sort."""
    for i in range(left + 1, right + 1):
        key = nums[i]
        j = i - 1
        while j >= left and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key


def merge(nums: List[int], left: int, mid: int, right: int) -> None:
    """Mezcla dos subarreglos ordenados en un solo subarreglo ordenado."""
    left_part = nums[left:mid + 1]
    right_part = nums[mid + 1:right + 1]
    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            nums[k] = left_part[i]
            i += 1
        else:
            nums[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        nums[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        nums[k] = right_part[j]
        j += 1
        k += 1


def tim_sort(arr: List[int]) -> List[int]:
    """Retorna una lista ordenada usando una versión simplificada de Tim Sort."""
    nums = arr.copy()
    n = len(nums)
    min_run = 32

    # Ordenar pequeños bloques usando insertion sort.
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort_range(nums, start, end)

    size = min_run
    # Mezclar bloques cada vez más grandes.
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                merge(nums, left, mid, right)
        size *= 2

    return nums


def main() -> None:
    ejemplo = [5, 21, 7, 23, 19, 10, 2, 16]
    print('Tim Sort')
    print('Entrada:', ejemplo)
    resultado = tim_sort(ejemplo)
    print('Salida ordenada:', resultado)
    print('Explicación: ordena bloques pequeños y luego los mezcla en bloques mayores.')


if __name__ == '__main__':
    main()
