import itertools

class ArithmeticProgression:

    def __init__(self, begin, stop, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index

    def artprog_gen(self, begin, step, end=None):
        first = type(begin + step)(begin)
        ap_gen = itertools.count(first, step)
        if end is not None:
            ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
        return ap_gen