"""Merge Sort - Ordenamiento por mezcla.
Divide el arreglo en subarreglos más pequeños y luego los combina.
"""

from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """Retorna una lista ordenada usando Merge Sort."""
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    izquierda = merge_sort(arr[:mid])
    derecha = merge_sort(arr[mid:])

    return merge(izquierda, derecha)


def merge(left: List[int], right: List[int]) -> List[int]:
    """Mezcla dos listas ordenadas en una sola lista ordenada."""
    resultado = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            resultado.append(left[i])
            i += 1
        else:
            resultado.append(right[j])
            j += 1

    resultado.extend(left[i:])
    resultado.extend(right[j:])
    return resultado


def main() -> None:
    ejemplo = [38, 27, 43, 3, 9, 82, 10]
    print('Merge Sort')
    print('Entrada:', ejemplo)
    resultado = merge_sort(ejemplo)
    print('Salida ordenada:', resultado)
    print('Explicación: divide en mitades, ordena cada mitad y las mezcla ordenadamente.')


if __name__ == '__main__':
    main()
