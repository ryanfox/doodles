# higher-order fibonacci-like functions


def f(n):
    cache = {i: 1 for i in range(n)}

    def g(m):
        if m not in cache:
            cache[m] = sum(g(i) for i in range(m - n, m))

        return cache[m]

    return g

if __name__ == '__main__':
    order = 5
    z = f(order)

    print("{}'th order fib sequence".format(order))
    for i in range(10):
        print(z(i))
