#!/usr/bin/python

# Functions to produce the powerset (all subsets)
# of a set of numbers

import sys

def update_ps(ps, e):
  newsets = []
  for m in ps:
    t = list(m)
    t.append(e)
    newsets.append(t)

  ps.extend(newsets)
  return ps

def powerset(s):
  ps = [[]]
  for x in s:
    ps = update_ps(ps, x)

  return ps

def main():
  prog_name = sys.argv[0]
  print ''

  if len(sys.argv) <  2:
    print 'Usage: ' + prog_name + ' elem [elem2] [elem3] [elem N]'
  else:
    elem_list = []
    for i in range(1, len(sys.argv)):
      elem_list.append(sys.argv[i])


    res = powerset(elem_list)
    print prog_name + '(' + str(elem_list) + ') => ' + str(res)

  print ''

main()

# end of file
