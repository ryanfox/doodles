# higher-order fibonacci-like functions


def f(n):
    cache = {i: 1 for i in range(n)}

    def g(m):
        if m not in cache:
            cache[m] = sum(g(i) for i in range(m - n, m))

        return cache[m]

    return g

if __name__ == '__main__':

    functions = 10
    parameters = 20

    results = []

    for i in range(1, functions + 1):
        func = f(i)
        results.append([func(j) for j in range(parameters)])

    width1 = len(str(functions))
    width2 = len(str(max([max(item) for item in results])))
    for i, result in enumerate(results):
            print('{:{width}} '.format(i + 1, width=width1) +
                  ' '.join('{:{width}}'.format(number, width=width2) for number in result))
