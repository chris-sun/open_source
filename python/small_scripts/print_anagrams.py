#!/usr/bin/python

# Function to primt all anagrams of a string
# Note a string might appear twice if the
# string has 2 or more of the same character

import sys

anagram_count = 0

def print_helper(prefix, suffix):
  global anagram_count
  #print 'ph(' + prefix + ', ' + suffix + ')'

  if len(suffix) < 2:
    print 'ANAGRAM: ' + prefix + suffix
    anagram_count += 1
  else:
    for i in range(0, len(suffix)):
      new_suffix = suffix[0:i] + suffix[i+1:]
      #print 'new_suffix: ' + new_suffix
      print_helper(prefix + suffix[i], new_suffix)

def print_anagrams(s):
  for i in range(0, len(s)):
    print_helper(s[i], s[0:i] + s[i+1:])

if len(sys.argv) != 2:
  print "Usage: %s STRING\n" % (sys.argv[0])
  sys.exit(1)

input = sys.argv[1]
print_anagrams(sys.argv[1])
print "Total anagrams for: '%s': %d" % (input, anagram_count)


