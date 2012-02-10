#!/usr/bin/python

# A few functions that implement binary search in an array



import sys

def i2c(w, n):
  return (n / w, n % w)

# This function implements binary search for a matrix.
# Right now it's hard coded to be a 5x5 matrix
def bs_matrix(a, n):
  a = []
  for i in range(0, 5):
    a.append([])
    for j in range(0, 5):
      a[i].append((i * 5) + j)

  min = 0
  max = 25 - 1
  loop_counter = 0

  print 'a: ' + str(a)

  while True:
    loop_counter += 1
    print 'Loop %d' % loop_counter

    if max < min:
      return -1
    i = (min + max) / 2
    (x, y) = i2c(5, i)

    print '  i: %d , a[%d][%d] = %d' % (i, x, y, a[x][y])
    if a[x][y] < n:
      min = i + 1
    elif a[x][y] > n:
      max = i - 1
    else:
      return i

# An iteravtive solution to binary search
def bs_iter(a, n):
  array_len = len(a)
  
  if array_len == 0:
    return -1 

  min = 0
  max = array_len - 1
  loop_counter = 0

  while True:
    loop_counter += 1
    print 'Loop %d' % loop_counter

    if max < min:
      return -1
    i = (min + max) / 2
    print 'a[%d] = %d' % (i, a[i])
    if a[i] < n:
      min = i + 1
    elif a[i] > n:
      max = i - 1
    else:
      return i


# This function splits stuff.
# So it cannot return the correct index
def bs(a, n):
  print '  bs called'
  array_len = len(a)
  
  if array_len == 0:
    return False 

  mid = array_len / 2

  if a[mid] == n:
    return True
  elif a[mid] < n:
    return bs(a[mid+1:], n)
  else:
    return bs(a[:mid], n)


def main():
  prog_name = sys.argv[0]
  print ''

  if len(sys.argv) < 2:
    print 'Usage: ' + prog_name + ' NUM1 [NUM2] [NUM3] ... [NUM X]'
  else:
    n = int(sys.argv[1])
    list = []
    num_args = len(sys.argv)
    for i in range(2, num_args):
      list.append(int(sys.argv[i]))

    res = bs_matrix(list, n)

    print prog_name + '(' + str(list) + ', ' + str(n) + ')'
    print '=> ' + str(res)

  print ''

main()

# end of file
