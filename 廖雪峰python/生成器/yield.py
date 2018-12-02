def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 5

o = odd()
next(o)
next(o)
next(o)

def fib(max):
    """斐波那契数列"""
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for n in fib(6):
    print(n)

g = fib(10)
while True:
    try:
        x = next(g)
        print('g:{0}'.format(x))
    except StopIteration as e:
        print('Generator return value: {0}'.format(e.value))
        break