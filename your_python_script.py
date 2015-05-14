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

