#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculator import add, sub
    if a < b:
        sums = add(a, b)
        for i in range(4, 6):
            sums = add (sums, i)
        return sums
        else:
            return sub(a, b)
