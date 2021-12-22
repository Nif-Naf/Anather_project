class Generation():

    def __init__(self, score):
        self.score = score

    def data_ver():
        """ """
        pass

    def gen_seq(self):
        """Generation of a super-growing sequence"""
        self.sequence = list([1])

        for i in range(self.score):
            res = sum(self.sequence) + 3
            self.sequence.append(res)

        return False #self.sequence

    def test(self):
        """ """
        total = 0
        for i in self.sequence:
            if i <= total:
                raise ValueError('Test failed.')

        return self.sequence

obj = Generation(10)
a = obj.gen_seq()
print(obj.test())
print(obj.gen_seq())

