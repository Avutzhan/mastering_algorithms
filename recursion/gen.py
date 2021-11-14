class Gen:
    """
    Class Gen = Generate numbers
    """
    data = []

    def gen_bin_recursive(self, M, prefix=""):
        if M == 0:
            self.data.append(prefix)
            return
        self.gen_bin_recursive(M - 1, prefix + "0")
        self.gen_bin_recursive(M - 1, prefix + "1")
        return self.data

    def gen_bin_iterative(self, M, prefix=""):
        if M == 0:
            self.data.append(prefix)
            return
        for digit in "0", "1":
            self.gen_bin_iterative(M - 1, prefix + digit)
        return self.data

    def generate_numbers(self, N: int, M: int, prefix=None):
        """
        Все перестановки
        Генерирует все числа (с лидирующими незначащими нулями) в N-ричной системе счисления
        N основание системы исчисления (N <= 10) длины M
        M количество чисел
        :param prefix:
        :param M: int
        :param N: int
        :return:
        """
        prefix = prefix or []
        if M == 0:
            self.data.append([x for x in prefix])  # prefix.copy() заменил на list comprehension
            return
        for digit in range(N):
            prefix.append(digit)
            self.generate_numbers(N, M - 1, prefix)
            prefix.pop()
        return self.data

    def clear_data(self):
        self.data = []
