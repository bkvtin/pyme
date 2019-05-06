#!/usr/bin/env python3

'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

'''
# -- https://hackernoon.com/prime-numbers-using-python-824ff4b3ea19
# -- fastest way to list all prime numbers
'''
def isprime_approach_fast(givenNumber):  
  primes = []
  for possiblePrime in range(2, givenNumber + 1):
    # Assume number is prime until shown it is not. 
    isPrime = True
    for num in range(2, int(possiblePrime ** 0.5) + 1):
      if possiblePrime % num == 0:
        isPrime = False
        break

    if isPrime:
        primes.append(possiblePrime)
  
  return(sum(primes))


'''
# slow function to list all prime number

def isprime_approach_slow(x):
  for i in range(2, (x//2 + 1)):
    if(x % i == 0):
      return False
      break
  else:
    return True

def prob_10(data):
  prime_numbers = 0
  for i in range(int(data)):
    if isprime_approach_slow(i):
      print(i)
      prime_numbers += 1
  return prime_numbers
'''


def main():
  data = 2000000
  result = isprime_approach_fast(data)
  print("Sum of all the primes below two million: ", result)


if __name__ == "__main__":
  main()