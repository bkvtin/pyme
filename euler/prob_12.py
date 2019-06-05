#!/usr/bin/env python3

import math

'''
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''


'''
# -- origin way but will take a lot of time and resource CPU

def triangle_number(data):
  if data > 0:
    return int(data * (data + 1) / 2)


def prob_12():
  count = 1
  while True:
    result = []
    num = triangle_number(count)

    for i in range(1, num):
      if num % i == 0:
        result.append(i)

    print("count day:", num, len(result))
    if len(result) >= 500:
      print(result)
      break
    else:
      count += 1
'''


'''
# new way, refer algorithm from https://www.mathblog.dk/triangle-number-with-more-than-500-divisors/
'''
def numOfDivisors(number):
  nod = 0;
  sqrt = int(math.sqrt(number))
  for i in range (1, sqrt):
    if number % i == 0:
      nod += 2
  
  # Correction if the number is a perfect square
  if sqrt * sqrt == number:
    nod -= 1

  return nod;


def prob_12():
  number = 0
  i = 1
  while numOfDivisors(number) < 500:
    number += i
    i += 1

  return number


def main():
  result = prob_12()
  print(result)


if __name__ == "__main__":
  main()
