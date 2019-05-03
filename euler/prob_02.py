#!/usr/bin/env python3

'''
def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)


l = []
for i in range(1,4000000):
    if fib(i) % 2 == 0:
        print("{}: {}".format(i, fib(i)))
        l.append(fib(i))


print(sum(l))
'''

a, b = 1, 1
total = 0
while a <= 4000000:
    if a % 2 == 0:
        total += a
    a, b = b, a+b  # the real formula for Fibonacci sequence
print(total)
