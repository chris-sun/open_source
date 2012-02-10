#!/usr/bin/python

# This is a solution to a problem
# where you have two arrays A and B
# A has a elements, B has b elements
# A has room for Ia + b) elements.
# Both arrays are sorted.
# Need to merge elements of B into the A array

import sys

def combine(a, b):
  i = len(a) - 1
  j = len(b) - 1
  c = []
  k = i + j + 1

  # Really only do this in Python
  for z in range(0, len(a) + len(b)):
    c.append(0)

  while i >=0 or j >= 0:
    if i < 0:
      c[k] = b[j]
      j -= 1
      k -= 1
      continue
    if j < 0:
      c[k] = a[i]
      i -= 1
      k -= 1
      continue

    if a[i] > b[j]:
      c[k] = a[i]
      i -= 1
      k -= 1
    else:
      c[k] = b[j]
      j -= 1
      k -= 1

  return c

def main():
  prog_name = sys.argv[0]
  print ''

  if len(sys.argv) != 3:
    print 'Usage: ' + prog_name + 'LIST1 LIST2'
  else:
    list1 = sys.argv[1].split(' ')
    list2 = sys.argv[2].split(' ')
    list1 = map(int, list1)
    list2 = map(int, list2)

    res = combine(list1, list2)

    print '=> ' + str(res)

  print ''

main()

# end of file
