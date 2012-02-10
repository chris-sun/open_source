#!/usr/bin/python

# Basic example of inheritance in python

class Employee:
    def __init__(self, name, salary = 0):
      self.name = name
      self.salary = salary

    def give_raise(self, percent):
      self.salary = self.salary + (self.salary * percent)

    def work(self):
      print self.name + " does stuff"

    def __repr__(self):
      return "Emp: name=%s, salary=%s" % (self.name, self.salary)

class Chef(Employee):
  def __init__(self, name):
    Employee.__init__(self, name, 50000)

  def work(self):
    print self.name + " cooks food"

class Athlete(Employee):
  def __init__(self, name):
    Employee.__init__(self, name, 5000000)

  def work(self):
    print self.name + " plays sports"

e = Employee('Joe', 20000)
c = Chef('Wolfgang')
a = Athlete('Lebron')

for o in [e, c, a]:
  print o

e.work()
c.work()
a.work()

