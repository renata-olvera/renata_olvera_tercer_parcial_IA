"""Heap Sort - Ordenamiento usando un heap máximo.
Convierte el arreglo en una estructura tipo árbol de montículo y extrae el mayor elemento.
"""

from typing import List


def heapify(arr: List[int], n: int, i: int) -> None:
    """Asegura que el subárbol con raíz en i satisface la propiedad de heap máximo."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr: List[int]) -> List[int]:
    """Retorna una lista ordenada usando Heap Sort."""
    nums = arr.copy()
    n = len(nums)

    # Construir el heap máximo desde abajo hacia arriba.
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)

    # Extraer elementos del heap y reconstruir el heap.
    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)

    return nums


def main() -> None:
    ejemplo = [12, 11, 13, 5, 6, 7]
    print('Heap Sort')
    print('Entrada:', ejemplo)
    resultado = heap_sort(ejemplo)
    print('Salida ordenada:', resultado)
    print('Explicación: construye un heap máximo y saca el mayor elemento repetidas veces.')


if __name__ == '__main__':
    main()
