# O(n log n)
def merge(A: list, B: list) -> list:
    C = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C


#  Recursive
def merge_sort(A):
    if len(A) <= 1:
        return
    middle = len(A) // 2
    L = [A[i] for i in range(0, middle)]
    R = [A[i] for i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    #  тут очень важный момент почему мы не сделали A = C хотя кажется было бы так легче,
    # потому что питон имеет ссылочную модель переменных и сборщик мусора
    # Например мы вызвали снаружи функцию B = [1, 2, 3] merge_sort(B) тут мы передали только ссылку на массив,
    # а в функции merge_sort B указывает на массив -> [1, 2, 3] внутри мы создали переменные L R C c массивами,
    # не экономили память могли бы съекономить. И если бы мы сделали A = C то просто перенесли бы указатель с А на С
    # сам массив А мы не изменили теперь А указывает на массив на который раньше указывал С но после выполнения функции
    # сборщик мусора удалит L R C и того массива на который указывает A больше не станет и в ответе выйдет ничего
    # чтобы не было такой проблемы мы просто копируем C в А
    for i in range(len(A)):
        A[i] = C[i]
        # перелили один массив в другой


# Toni Hoar Sort == quick_sort
def quick_sort(A):
    if len(A) <= 1:
        return
    barrier = A[0]
    L = []
    M = []
    R = []
    # L = M = R = [] список является обьектом из за ссылочной модели тут три переменных указывают на один обьект списка
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    quick_sort(L)
    quick_sort(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1



