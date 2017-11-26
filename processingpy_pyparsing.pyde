"""
Parsing in Processing.py with pyparsing: a simple example 

This example is drawn from John Strickler's article "Parseltongue":
https://www.accelebrate.com/blog/pyparseltongue-parsing-text-with-pyparsing/

It defines a simple parser to identify and extract
US Social Security Numbers (SSNs).

    grammar:
    ssn ::= nums+ '-' nums+ '-' nums+
    nums ::= '0' | '1' | '2' etc etc

"""

from pyparsing import *

dash = '-'

ssn_parser = Combine(
    Word(nums, exact=3)
    + dash
    + Word(nums, exact=2)
    + dash
    + Word(nums, exact=4)
)

input_string = """
    xxx 225-92-8416 yyy
    103-33-3929 zzz 028-91-0122
"""

for match, start, stop in ssn_parser.scanString(input_string):
    print(match, start, stop)
