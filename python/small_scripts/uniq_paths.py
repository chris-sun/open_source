#!/usr/bin/python

# A commonly asked question:
# Find number of unique paths in a grid
# if you start on the northwest corner
# and want to go to the southeast corner
# by only moving to the left and down.

import sys
import time

path_hash = {}

def get_hash_key(x, y):
  return str(x) + ':' + str(y)

def uniq_paths(x, y):
  global path_hash
  use_table = True

  if x < 0 or y < 0:
    return 0
  if x == 0 or y == 0:
    return 1
  else:
    if not use_table:
      return uniq_paths(x - 1, y) + uniq_paths(x, y - 1)
    else:
      key = get_hash_key(x, y)
      value = path_hash.get(key)
      if value:
        return value
      else:
        n = uniq_paths(x - 1, y) + uniq_paths(x, y - 1)
        path_hash[key] = n
        return n

def main():
  prog_name = sys.argv[0]
  print ''

  if len(sys.argv) != 3:
    print 'Usage: ' + prog_name + ' width height'
  else:

    start_time = time.time()
    res = uniq_paths(int(sys.argv[1]), int(sys.argv[2]))
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000.0

    print prog_name + '(' + sys.argv[1] + ', ' + sys.argv[2] + ') => ' + str(res)
    print '%s took %0.3f ms' % (prog_name, elapsed_time)

  print ''

main()

# end of file
