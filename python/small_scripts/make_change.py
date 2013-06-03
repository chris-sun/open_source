#!/usr/bin/python

# Given a certain amount of money M,
# how many ways are there to make change
# (in quarters, dimes, nickels, pennies)
# for that amount M

import sys

def make_change(goal, denom, tabs=0):
  #print '%s mc(%d, %d)' % ('  ' * tabs, goal, denom)
  ways = 0
  next_denom = 0

  if 25 == denom:
    next_denom = 10
  elif 10 == denom:
    next_denom = 5
  elif 5 == denom:
    next_denom = 1
  else:
    return 1

  i = 0
  product = 0
  while product <= goal:
    ways += make_change(goal - product, next_denom, tabs + 1)
    i += 1
    product = i * denom
   
  return ways

"""
if len(sys.argv) > 1:
  res = make_change(int(sys.argv[1]), 25)
  print sys.argv[0] + '(' + sys.argv[1] + ') => ' + str(res)
else:
  print 'Usage: ' + sys.argv[0] + ' NUM'
"""

for i in range(1, 118):
  res = make_change(i, 25)
  print sys.argv[0] + '(' + str(i) + ') => ' + str(res)


