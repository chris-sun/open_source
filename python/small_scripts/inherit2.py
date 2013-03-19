#!/usr/bin/python

import sys

class Athlete:
  def __init__(self, sport):
    self.sport = "athlete"

  def talk(self):
    print "I am a %s" % (self.sport)

  # override this method
  def show_sport(self):
    print "I play %s" % (self.sport)

class Runner(Athlete):
  def __init__(self, sport, shoe_size):
    Athlete.__init__(self, sport)
    self.shoe_size = shoe_size

  def show_sport(self):
    print "I'm a runner you fools!"

a = Athlete("whatever")
r = Runner("running", 9)
a.talk()
r.talk()
a.show_sport()
r.show_sport()
print a.__class__
print r.__class__

