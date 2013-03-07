#!/usr/bin/python
# This program assumes at least Python 2.6 or higher
# to support builtin namespace for "set"

"""
BIT PERFECT

Define a number as "bit-perfect" if the number of 1 bits in its binary 
representation is a perfect square.  For example, 1 and 15 are both bit-perfect.

Design and implement a function pb_window(a, b), preferably in python, that 
returns the number of bit-perfect numbers in range [a, b], inclusive, with a > 0.
For example, pb_window(99, 99999) should return 20422.
"""

import sys
import time
from math import factorial

# These globals are used by the function is_square()
next_adden = 13
max_square = 36
# An initial set of perfect squares.  Will update this set as needed
square_set = set([1, 4, 9, 16, 25, 36])

# Return true if N is a perfect square (i.e. 1, 4, 9, 16, 25)
# Otherwise return false
def is_square(n):
  global next_adden
  global max_square
  global square_set

  # Check if number is in the dictionary of known square values
  if n <= max_square:
    if n in square_set:
      return True
    else:
      return False
  else:
    while n > max_square:
      max_square += next_adden
      next_adden += 2
      square_set.add(max_square)
      if n == max_square:
        return True
  
  return False

def combination(n, r):
  return factorial(n) / (factorial(r) * factorial(n-r))

# Decorator function for timing tests
def timing_decorator(func):
  def wrapper(*arg):
    start_time = time.time()
    res = func(*arg)
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000.0
    print '%s took %0.3f ms' % (func.func_name, elapsed_time)
    return res

  return wrapper

def is_bit_perfect(n):
  one_bits = num_one_bits(n)
  return is_square(one_bits)
  
def num_one_bits(n):
  return bin(n).count('1')

@timing_decorator
def cube(x):
  return x * x * x

def bit_length(x):
  return len(bin(x)) - 2

def pb_brute_force(a, b):
  total = 0
  while a <= b:
    total += is_bit_perfect(a)
    a += 1

  return total

def pb_improved(a, b):
  lower_bit_length = bit_length(a)
  upper_bit_length = bit_length(b)

  total = 0
  temp_total = 0
  current_square = 4
  adden = 5

  for i in range(lower_bit_length, upper_bit_length + 1):
    current_square = 4
    adden = 5

    #print 'i: ' + str(i)
    if i == lower_bit_length:
      temp_max = (2 ** lower_bit_length) - 1
      temp_total = pb_brute_force(a, temp_max)
      #print '... pb_brute(' + str(a) + ', ' + str(temp_max) + ') => ' + str(temp_total)
      total += temp_total
      continue

    if i == upper_bit_length:
      temp_min = (2 ** (upper_bit_length - 1))
      temp_total = pb_brute_force(temp_min, b)
      #print '... pb_brute(' + str(temp_min) + ', ' + str(b) + ') => ' + str(temp_total)
      total += temp_total
      continue

    # For certain bit lengths, we computes the combinations of bit strings
    # that can have 1 one bit, 4 one bits, or 9 one bits, or 16 one bits, 
    # or X one bits (where X is a perfect square)

    # A binary number of length N, has exactly 1 possible number
    # That can have 1 one bit.  In this case, the one bit
    # is at the most significant position.
    total += 1

    # This is a shortcut.  I know it advance that
    # bit strings of length 1, 2, 3 cannot have 4 one bits
    # They can only have 1 bit perfect number.
    if i < 4:
      continue

    # When looking for binary numbers with R one bits, where R > 1
    # we can use combinations C(N, R).
    # Since every binary number beings with a 1 bit,
    # I'm actually computing C(N-1, R-1), where N is the number
    # of bits in a binary number, and R is a perfect square.
    while i >= current_square:
      n = i - 1
      r = current_square - 1
      # pang
      temp_total = combination(n, r)
      #print '..... C(' + str(n) + ', ' + str(r) + ') => ' + str(temp_total)
      total += temp_total
      # Find the next perfect square
      current_square += adden
      adden += 2

  return total

    

@timing_decorator
def pb_window(a, b):
  use_brute_force = False
  #use_brute_force = True

  # pb_improved is a faster method, since it doesn't count the bits
  # of every number in the range.  Instead, for certain ranges
  # it computes the possible number of combinations of numbers
  # that can have 4 one bits, or 9 one bits, or 16 one bits, or X one bits
  if use_brute_force:
    return pb_brute_force(a, b)
  else:
    return pb_improved(a, b)

def main():
  if len(sys.argv) != 3:
    print ''
    print 'Usage: python ./bit_perfect.py LOW_NUM HIGH_NUM'
    print ''
  else:
    res = pb_window(int(sys.argv[1]), int(sys.argv[2]))
    print 'pb_window(' + sys.argv[1] + ', ' + sys.argv[2] + ') => ' + str(res)

main()

# end of file
