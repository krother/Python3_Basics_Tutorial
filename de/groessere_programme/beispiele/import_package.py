"""
Code modularization by importing from a package.
"""
# a package is simply a directory with Python modules.
# The module __init__.py is obligatory,
# and it is imported automatically

from calculations import addition
from calculations.multi import multiply
# note the two different ways the functions are imported.
# Check calculations/__init__.py to find out how 'addition()'' is located

print(addition(3, 4))
print(multiply(3, 4))
