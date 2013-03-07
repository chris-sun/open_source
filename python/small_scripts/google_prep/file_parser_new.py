#!/usr/bin/python

import re
import sys

artist_hash = {}
line_count = 0

if len(sys.argv) < 2:
  print "Usage: %s INPUT_FILE\n" % sys.argv[0]
  sys.exit(1)

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

sorted_list = sorted(artist_hash, key=artist_hash.get, reverse=True)
for a in sorted_list:
  print "%s has %d top songs" % (a, artist_hash[a])
      
