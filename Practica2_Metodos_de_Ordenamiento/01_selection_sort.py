"""Selection Sort - Ordenamiento por selección.
Selecciona el elemento más pequeño del segmento restante y lo coloca al frente.
"""

from typing import List


def selection_sort(arr: List[int]) -> List[int]:
    """Retorna una nueva lista ordenada usando Selection Sort."""
    # Copiamos la lista para no modificar la entrada original.
    nums = arr.copy()
    n = len(nums)

    # Recorremos cada posición del arreglo.
    for i in range(n):
        min_idx = i  # Suponemos que el elemento actual es el mínimo.
        # Buscamos el valor mínimo entre los elementos restantes.
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        # Intercambiamos el elemento actual con el mínimo encontrado.
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums


def main() -> None:
    ejemplo = [29, 10, 14, 37, 13]
    print('Selection Sort')
    print('Entrada:', ejemplo)
    resultado = selection_sort(ejemplo)
    print('Salida ordenada:', resultado)
    print('\nExplicación: cada iteración coloca el elemento más pequeño del resto en la posición correcta.')


if __name__ == '__main__':
    main()
