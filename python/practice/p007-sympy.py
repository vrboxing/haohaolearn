#! /usr/bin/python3
# -*- coding: utf-8 -*-

# import os
# import sys
# import datetime
# import argparse
from sympy.solvers import solve
from sympy import Symbol

if __name__ == '__main__':

    x = Symbol('x')
    print(solve(x**3 - 2 * x**2 - 1, x))