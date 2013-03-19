#!/usr/bin/python

import sys

class LL:

  def __init__(self, n):
    self.n = n
    self.next = None

  def append(self, l2):
    curr = self
    while curr.next != None:
      curr = curr.next
    curr.next = l2

  def reverse(self):
    curr = self
    prev = None

    while curr != None:
      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp

    self = prev

  def show(self):
    curr = self
    while curr != None:
      sys.stdout.write("%d " % (curr.n))
      curr = curr.next
    print ""

l = LL(3)
l.append(LL(1))
l.append(LL(4))
l.append(LL(1))
l.append(LL(5))
l.append(LL(9))
l.append(LL(2))
l.append(LL(6))
l.append(LL(5))

l.show()
l.reverse()
l.show()
