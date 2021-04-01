# -*- coding: utf-8 -*-
import sys

fname_r = "popular-names.txt"

n = sys.argv[-1]
while not(n.isdigit()):
    n = input('Input number >')
n = int(n)

with open(fname_r, mode="r") as f:
    datalines = f.readlines()[-n:]
print(''.join(datalines))
