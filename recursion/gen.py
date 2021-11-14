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

    def clear_data(self):
        self.data = []
