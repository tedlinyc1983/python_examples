Yes:
import os
import sys

No:
import sys, os

standard library imports

related third party imports

local application/library specific imports

Yes:
x = 1
y = 2
long_variable = 3

No:
x    = 1
y    = 2
long_variable = 3

Yes:
def complex(real, imag=0.0):
  return magic(r=real, i=imag)

No:
def complex(real, imag = 0.0):
  return magic(r = real, i = imag)

if valid():
    print 'valid'

if not valid():
    print 'invalid'

if not users:
    print 'No users available'

if i % 2 == 0:
    print 'even number'


class Negator(object):
    def __eq__(self, other):
        return not other

thing = Negator()
print thing == None

print thing is None
