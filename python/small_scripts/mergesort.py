#!/usr/bin/python

# Python implementation of mergesort

import sys

def merge(left, right):
  print 'merge(' + str(left) + ', ' + str(right) + ')'
  res = []
  i = 0
  j = 0
  left_len = len(left)
  right_len = len(right)

  while i < left_len or j < right_len:
    if i == left_len:
      res.append(right[j])
      j += 1
      continue

    if j == right_len:
      res.append(left[i])
      i += 1
      continue

    if left[i] <= right[j]:
      res.append(left[i])
      i += 1
    else:
      res.append(right[j])
      j += 1

  return res

def mergesort(lst):
  size = len(lst)
  if size < 2:
    return lst
  else:
    middle = size / 2
    left_list = mergesort(lst[:middle])
    right_list = mergesort(lst[middle:])
    return merge(left_list, right_list)

def main():
  prog_name = sys.argv[0]
  print ''

  if len(sys.argv) < 2:
    print 'Usage: ' + prog_name + ' NUM1 [NUM2] [NUM3] ... [NUM X]'
  else:
    list = []
    num_args = len(sys.argv)
    for i in range(1, num_args):
      list.append(int(sys.argv[i]))

    res = mergesort(list)

    print prog_name + '(' + str(list) + ')'
    print '=> ' + str(res)

  print ''

main()

# end of file
