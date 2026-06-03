"""Quick Sort - Ordenamiento rápido.
Usa un pivote para dividir el arreglo en menores, iguales y mayores.
"""

from typing import List


def quick_sort(arr: List[int]) -> List[int]:
    """Retorna una lista ordenada usando Quick Sort."""
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[len(arr) // 2]
    menores = [x for x in arr if x < pivot]
    iguales = [x for x in arr if x == pivot]
    mayores = [x for x in arr if x > pivot]

    # Ordenar recursivamente las partes menores y mayores.
    return quick_sort(menores) + iguales + quick_sort(mayores)


def main() -> None:
    ejemplo = [10, 7, 8, 9, 1, 5]
    print('Quick Sort')
    print('Entrada:', ejemplo)
    resultado = quick_sort(ejemplo)
    print('Salida ordenada:', resultado)
    print('Explicación: elige un pivote y divide el conjunto en menores, iguales y mayores.')


if __name__ == '__main__':
    main()
