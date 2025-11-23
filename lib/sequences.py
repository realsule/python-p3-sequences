#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return

    fib = [0, 1, 1, 2, 3, 5, 8, 13, 21]
    while len(fib) < length:
        fib.append(fib[-1] + fib[-2])

    print(fib[:length])

    