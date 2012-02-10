#!/usr/bin/python

# Given a number is based 2,
# add 1 to that number.
# ternary_incr( ) returns that result of that sum

import sys

def ternary_incr(s):

  has_carry = True
  res = ''

  last_index = len(s) - 1
  for i in range(last_index, -1, -1):
    if has_carry:
      if s[i] == '2':
        has_carry = True
        res = '0' + res
      else:
        has_carry = False
        res = str(int(s[i]) + 1) + res
    else:
        res = s[i] + res

  if has_carry:
    res = str(1) + res

  return res

def main():
  if len(sys.argv) == 2:
    result = ternary_incr(sys.argv[1])
    print "ternary_incr(%s) => %s" % (sys.argv[1], result)

main()
