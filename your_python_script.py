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

if name in ('Alice', 'Bob', 'Charlie'):
    print 'ok'

if name == 'Alice' or name == 'Bob' or name == 'Charlie':
    print 'ok

msg = 'Hello world'
if 'world' in msg:
    print 'find it'


msg = 'Hello world'
if msg.find('world') != -1:
    print 'find it'


t = 12345, 54321, 'hello!'
x, y, z = t

my_list = ['Alice', 12, 'Python']
(name, age, skill) = my_list


my_list = ['Alice', 12, 'Python']
name = my_list[0]
age = my_list[1]
skill = my_list[2]

(x, y) = (y, x)

def get_error_details():
    return (2, 'details')

(errnum, errstr) = get_error_details()
