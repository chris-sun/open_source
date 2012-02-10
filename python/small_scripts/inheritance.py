#!/usr/bin/python

# Another example of inheritance in Python

class Superclass:
  name = ''

  def __init__(self, name):
    self.name = name

  def talk(self):
    print 'I am Superclass, hear me roar'

  def show_name(self):
    print 'My name is: ' + self.name

class Subclass(Superclass):
  college = ''

  def __init__(self, name, college):
    Superclass.__init__(self, name)
    self.college = college

  def talk(self):
    print 'I am a college graduate.  I went to ' + self.college

  def brag(self):
    print 'I like to brag that I went to ' + self.college
    

c1 = Superclass('Joe')
c2 = Subclass('Barack', 'Harvard')

c1.show_name()
c2.show_name()

c1.talk()
c2.talk()

c2.brag()
