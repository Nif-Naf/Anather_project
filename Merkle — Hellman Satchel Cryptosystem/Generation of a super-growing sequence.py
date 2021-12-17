class Generation():

    def __init__(self, score):
        self.score = score

    def data_ver():
        """ """
        pass

    def gen_seq(score_ver):
        """Generation of a super-growing sequence"""
        sequence = list([1])

        for i in range(score_ver):
            res = sum(sequence) + 3
            sequence.append(res)

        return sequence

    def test(sequence):
        """ """
        total = 0
        result = 'Test succesful.'
        for i in sequence:
            """ """
            if i <= total:
                raise ValueError('Test failed.')

        return result

    def autotest():
        """ """
        pass


obj = Generation
a = obj.gen_seq(10)
print(a)
print(obj.test(a))

print(Generation.gen_seq(10))