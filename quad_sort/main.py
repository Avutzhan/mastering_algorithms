# quadratic sorting algos
# O (N^2)

def insert_sort(A: list) -> list:
    """
    Сортировка списка А вставками
    :param A: list
    :return: A: list
    """
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k - 1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1
    return A


def selection_sort(A: list) -> list:
    """
    Сортировка списка А выбором
    :param A: list
    :return: A: list
    """
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]
    return A


def bubble_sort(A):
    """
    Сортировка списка А методом пузырька
    :return:
    """
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]
    return A
