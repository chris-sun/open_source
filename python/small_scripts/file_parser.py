#!/usr/bin/python

# A basic file parser.
# In this case it returns music artists
# with the most #1 hit songs in 2011.
# The input file is topsongs2011.txt
# which is in this directory

import re
import sys

artist_hash = {}

line_count = 0
handle = open(sys.argv[1], "r")
for line in handle:
  line = line.rstrip()
  if '#' == line[0]:
    continue
  else:
    m = re.match(r'(\d+.\s+)(.*)(\s+)"(.*)', line)
    if None != m:
      line_count += 1
      artist = m.group(2)

      if artist in artist_hash:
        artist_hash[artist] += 1
      else:
        artist_hash[artist] = 1

for a in sorted(artist_hash, key=artist_hash.get, reverse=True):
  print(a, artist_hash[a])

