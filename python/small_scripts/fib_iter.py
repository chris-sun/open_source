#!/usr/bin/python

# Print out the Fibonacci numbers
# where fib(1) = 1
# and fib(2) = 1
# Assuming input is always greater than 0

import sys

def fib(n):
  if n < 3:
    return 1

  a = 1
  b = 1
  total = 0

  for i in range(2, n):
    total = a + b
    a = b
    b = total

  return total

if len(sys.argv) > 1:
  res = fib(int(sys.argv[1]))
  print sys.argv[0] + '(' + sys.argv[1] + ') => ' + str(res)
else:
  print 'Usage: ' + sys.argv[0] + ' NUM'


