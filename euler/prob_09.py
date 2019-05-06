#!/usr/bin/env python3

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
flag = 0
a=1
while flag is 0:
    print("a",a)
    for i in range(a, a+1):
        print("i",i)
        if i**2 + (i+1)**2 == (i+2)**2:
            if (i + 1)*3 == 1000:
                print(a)
                flag = 1
                break
    else:
        a+=1
