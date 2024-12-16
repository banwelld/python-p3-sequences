#!/usr/bin/env python3

def fib_seq(length):
    new_seq = []
    for i in range(length):
        element_value = i if i < 2 else sum(new_seq[-1:-3:-1])
        new_seq.append(element_value)
    return new_seq    

def print_fibonacci(length):
    if not length:
        print([])
    else:
        print(fib_seq(length))