# -*- coding: utf-8 -*-
import re
import sys

fname_r = "popular-names.txt"

with open(fname_r, mode="r") as f:
    datalines = f.readlines()

n = sys.argv[-1]
while not(n.isdigit()):
    n = input('Input number >')
n = int(n)
print(''.join([line for line in datalines[:n]]))
