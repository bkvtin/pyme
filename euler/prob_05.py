#!/usr/bin/env python3

'''
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

num = 1
def exe():
    num = 1
    while True:
        count = 0
        for i in range (1, 21):
            if num % i == 0:
                count += 1

        if count == 20:
           break
        else:
           num += 1

exe()
