#!/usr/bin/env python2.4
# Эта программа показыает работу декоратора, который производит оптимизацию хвостового вызова. Он делает это, вызывая исключение, если оно является его прародителем, и перехватывает исключения, чтобы вызвать стек.

import sys
import timeit


class TailRecurseException(Exception):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(g):

    def func(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
            raise TailRecurseException(args, kwargs)
        else:
            while 1:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException as e:
                    args = e.args
                    kwargs = e.kwargs
    func.__doc__ = g.__doc__
    return func


@tail_call_optimized
def factorial(n, acc=1):
    if n == 0:
        return acc
    return factorial(n-1, n*acc)


print(f'{timeit.timeit(lambda: factorial(1000, 1), number=10000)}\n')