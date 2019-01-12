import time



def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print('%r => %2.2f ms' % (method.__name__, (te - ts) * 1000))
        return result

    return timed



@timeit
def using_comprehension(numbers) -> list:
    return [k / 2 for k in [j * 10 for j in [i + 1 for i in numbers]]]


@timeit
def using_generators(numbers) -> list:
    return list((k / 2 for k in (j * 10 for j in (i + 1 for i in numbers))))


if __name__ == '__main__':
    r = range(0, 20_000)
    _comprehension = using_comprehension(r)
    _generator = using_generators(r)
