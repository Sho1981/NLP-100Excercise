# -*- coding: utf-8 -*-

fname_r = "popular-names.txt"

with open(fname_r, mode="r") as f:
    col1 = [line.split()[0] for line in f.readlines()]

print(sorted(set(col1)))