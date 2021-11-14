print('manual test begin')

# def generate_numbers(N: int, M: int, prefix=None):
#     """
#     Все перестановки
#     Генерирует все числа (с лидирующими незначащими нулями) в N-ричной системе счисления
#     N основание системы исчисления (N <= 10) длины M
#     M количество чисел
#     :param prefix:
#     :param M: int
#     :param N: int
#     :return:
#     """
#     prefix = prefix or []
#     if M == 0:
#         print(prefix)
#         return
#     for digit in range(N):
#         prefix.append(digit)
#         generate_numbers(N, M-1, prefix)
#         prefix.pop()
#
#
# generate_numbers(3, 3)


# def finder(num: int, A: list) -> bool:
#     """
#     Ищет x в A и возвращает True, если такой есть False, если такого нет
#     :param num:
#     :param A:
#     :return: bool
#     """
#     for x in A:
#         if num == x:
#             return True
#     return False
#
#
# def generate_permutations(N: int, M: int = -1, prefix=None):
#     """
#     Генерация всех перестановок N чисел в M позициях,
#     с префиксом prefix
#     :param prefix:
#     :param M: int
#     :param N: int
#     :return:
#     """
#     M = N if M == -1 else M  # по умолчанию N чисел в N позициях
#     prefix = prefix or []
#     if M == 0:
#         print(prefix)
#         return
#     for number in range(1, N + 1):
#         if finder(number, prefix):
#             continue
#         prefix.append(number)
#         generate_permutations(N, M - 1, prefix)
#         prefix.pop()
#
#
# generate_permutations(3)
