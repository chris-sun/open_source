#!/usr/bin/python

# A function to shuffle cards,
# where each possible deck has the same
# chance of appearing.
# In other words a shuffle that is statistically significant
# and random for any given shuffle.

import random

def shuffle(num_cards):
  temp = 0
  index = 0
  cards = range(0, num_cards)

  print 'Before shuffle: ' + str(cards)

  for i in range(0, num_cards):
    rand_num = random.randint(0, num_cards - 1 - i)
    index = i + rand_num
    temp = cards[i]
    cards[i] = cards[index]
    cards[index] = temp

  print '-' * 10
  print 'After shuffle: ' + str(cards)

shuffle(52)

