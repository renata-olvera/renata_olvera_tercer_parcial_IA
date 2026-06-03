"""Bucket Sort - Ordenamiento por cubetas.
Distribuye valores en cubetas y ordena cada cubeta por separado.
"""

from typing import List


def bucket_sort(arr: List[float]) -> List[float]:
    """Retorna una lista ordenada usando Bucket Sort."""
    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # Colocar cada valor en una cubeta según su posición relativa.
    for num in arr:
        index = int((num - min_val) / (max_val - min_val + 1e-9) * (bucket_count - 1))
        buckets[index].append(num)

    # Ordenar cada cubeta individualmente.
    for bucket in buckets:
        bucket.sort()

    resultado = []
    for bucket in buckets:
        resultado.extend(bucket)

    return resultado


def main() -> None:
    ejemplo = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    print('Bucket Sort')
    print('Entrada:', ejemplo)
    resultado = bucket_sort(ejemplo)
    print('Salida ordenada:', resultado)
    print('Explicación: agrupa valores en cubetas y ordena cada cubeta por separado antes de unirlas.')


if __name__ == '__main__':
    main()
