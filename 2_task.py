#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit


class recursion(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        while callable(result): result = result()
        return result

    def call(self, *args, **kwargs):
        return lambda: self.func(*args, **kwargs)


@recursion
def factorial_opt(n, acc=1):
    if n == 0:
        return acc
    return factorial(n-1, n*acc)
    

def factorial(n, acc=1):
    if n == 0:
        return acc
    return factorial(n-1, n*acc)

if __name__ == '__main__':
    print("Время работы кода с использованием интроспекции")
    print(f'{timeit.timeit(lambda: factorial_opt(250), number=10000)}\n')
    print("Время работы кода без использования интроспекции")
    print(timeit.timeit(lambda: factorial(250), number=10000))
    
