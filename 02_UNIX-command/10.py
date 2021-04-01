# -*- coding: utf-8 -*-

fname_r = "popular-names.txt"

with open(fname_r, mode="r") as f:
    datalines = f.readlines()
print(len(datalines))
