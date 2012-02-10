#!/usr/bin/python

# Function to primt all anagrams of a string
# Note a string might appear twice if the
# string has 2 or more of the same character

import sys

anagram_count = 0

def print_helper(p, s):
  global anagram_count
  print 'ph(' + p + ', ' + s + ')'

  if len(s) < 2:
    print 'ANAGRAM: ' + p + s
    anagram_count += 1
  else:
    for i in range(0, len(s)):
      new_suffix = s[0:i] + s[i+1:]
      #print 'new_suffix: ' + new_suffix
      print_helper(p + s[i], new_suffix)

def print_anagrams(s):
  for i in range(0, len(s)):
    print_helper(s[i], s[0:i] + s[i+1:])

input = sys.argv[1]
print_anagrams(sys.argv[1])
print 'Total anagrams for: ' + input
print str(anagram_count)


