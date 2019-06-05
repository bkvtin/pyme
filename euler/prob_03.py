#!/usr/bin/env python3

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def isprime_approach_slow(x):
  for i in range(2, (x//2 + 1)):
    if(x % i == 0):
      return False
      break
  else:
    return True

def test(data):
  print(":: Processing ", data)

  for i in range(2, int(data ** 0.5) + 1):
    if data % i == 0:
      return False
      break
  else:
  	return True


def prob_03(data): 
  result = []
  for i in range(1, data):
    if data % i == 0 and test(i):
      print(i)
      result.append(i)    
  return result


def main():
  data = 600851475143
  #data = 90
  print(prob_03(data))


if __name__ == "__main__":
  main()