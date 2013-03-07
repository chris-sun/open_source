#!/usr/bin/python

import sys

num_args = len(sys.argv)
print "%d command line args" % (num_args)

i = 0
for arg in sys.argv:
  print "sys.argv[%d] = %s" % (i, sys.argv[i])
  i += 1

